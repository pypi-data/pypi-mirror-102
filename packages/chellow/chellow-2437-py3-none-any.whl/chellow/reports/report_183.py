import csv
import os
import sys
import threading
import traceback
import zipfile
from io import StringIO

from flask import g, request

from sqlalchemy import or_
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.expression import null, true

import chellow.dloads
from chellow.models import Era, Session, Site, SiteEra, Supply
from chellow.utils import ct_datetime, hh_format, req_date, req_int, to_ct, to_utc
from chellow.views import chellow_redirect


def none_content(site_id, start_date, finish_date, user, file_name):
    sess = zf = None
    try:
        sess = Session()
        running_name, finished_name = chellow.dloads.make_names(file_name, user)
        sites = (
            sess.query(Site)
            .join(SiteEra)
            .join(Era)
            .filter(
                SiteEra.is_physical == true(),
                or_(Era.finish_date == null(), Era.finish_date >= start_date),
                Era.start_date <= finish_date,
            )
        )
        zf = zipfile.ZipFile(running_name, "w")

        start_date_str = hh_format(start_date)
        finish_date_str = hh_format(finish_date)
        for site in sites:
            buf = StringIO()
            writer = csv.writer(buf, lineterminator="\n")
            writer.writerow(
                [
                    "Site Code",
                    "Site Name",
                    "Associated Site Codes",
                    "Sources",
                    "Generator Types",
                    "From",
                    "To",
                    "Type",
                    "Date",
                ]
                + list(map(str, range(1, 51)))
            )
            associates = " ".join(
                s.code for s in site.find_linked_sites(sess, start_date, finish_date)
            )
            source_codes = set()
            gen_types = set()
            for supply in (
                sess.query(Supply)
                .join(Era)
                .join(SiteEra)
                .filter(
                    SiteEra.is_physical == true(),
                    SiteEra.site == site,
                    Era.start_date <= finish_date,
                    or_(Era.finish_date == null(), Era.finish_date >= start_date),
                )
                .distinct()
                .options(joinedload(Supply.source), joinedload(Supply.generator_type))
            ):
                source_codes.add(supply.source.code)
                gen_type = supply.generator_type
                if gen_type is not None:
                    gen_types.add(gen_type.code)
            source_codes_str = ", ".join(sorted(source_codes))
            gen_types_str = ", ".join(sorted(gen_types))
            row = None
            for hh in site.hh_data(sess, start_date, finish_date):
                ct_start_date = to_ct(hh["start_date"])
                if ct_start_date.hour == 0 and ct_start_date.minute == 0:
                    if row is not None:
                        writer.writerow(row)
                    row = [
                        site.code,
                        site.name,
                        associates,
                        source_codes_str,
                        gen_types_str,
                        start_date_str,
                        finish_date_str,
                        "used",
                        ct_start_date.strftime("%Y-%m-%d"),
                    ]
                used_gen_kwh = hh["imp_gen"] - hh["exp_net"] - hh["exp_gen"]
                used_3p_kwh = hh["imp_3p"] - hh["exp_3p"]
                used_kwh = hh["imp_net"] + used_gen_kwh + used_3p_kwh
                row.append(str(round(used_kwh, 2)))
            if row is not None:
                writer.writerow(row)
            zf.writestr(
                site.code + "_" + finish_date.strftime("%Y%m%d%M%H") + ".csv",
                buf.getvalue(),
            )

            # Avoid long-running transaction
            sess.rollback()
    except BaseException:
        msg = traceback.format_exc()
        sys.stderr.write(msg)
        zf.write(msg)
    finally:
        if sess is not None:
            sess.close()
        if zf is not None:
            zf.close()
            os.rename(running_name, finished_name)


def site_content(site_id, start_date, finish_date, user, file_name):
    sess = f = None
    try:
        sess = Session()
        running_name, finished_name = chellow.dloads.make_names(file_name, user)
        f = open(running_name, mode="w", newline="")
        writer = csv.writer(f, lineterminator="\n")
        site = Site.get_by_id(sess, site_id)
        sites = sess.query(Site).filter(Site.id == site_id)
        start_date_str = hh_format(start_date)
        finish_date_str = hh_format(finish_date)

        for site in sites:
            writer.writerow(
                [
                    "Site Code",
                    "Site Name",
                    "Associated Site Codes",
                    "Sources",
                    "Generator Types",
                    "From",
                    "To",
                    "Type",
                    "Date",
                ]
                + list(map(str, range(1, 51)))
            )
            associates = " ".join(
                s.code for s in site.find_linked_sites(sess, start_date, finish_date)
            )
            source_codes = set()
            gen_types = set()
            for supply in (
                sess.query(Supply)
                .join(Era)
                .join(SiteEra)
                .filter(
                    SiteEra.is_physical == true(),
                    SiteEra.site == site,
                    Era.start_date <= finish_date,
                    or_(Era.finish_date == null(), Era.finish_date >= start_date),
                )
                .distinct()
                .options(joinedload(Supply.source), joinedload(Supply.generator_type))
            ):
                source_codes.add(supply.source.code)
                gen_type = supply.generator_type
                if gen_type is not None:
                    gen_types.add(gen_type.code)
            source_codes_str = ", ".join(sorted(source_codes))
            gen_types_str = ", ".join(sorted(gen_types))
            vals = None
            for hh in site.hh_data(sess, start_date, finish_date):
                hh_start_ct = to_ct(hh["start_date"])
                if hh_start_ct.hour == 0 and hh_start_ct.minute == 0:
                    if vals is not None:
                        writer.writerow(vals)
                    vals = [
                        site.code,
                        site.name,
                        associates,
                        source_codes_str,
                        gen_types_str,
                        start_date_str,
                        finish_date_str,
                        "used",
                        hh_start_ct.strftime("%Y-%m-%d"),
                    ]
                used_gen_kwh = hh["imp_gen"] - hh["exp_net"] - hh["exp_gen"]
                used_3p_kwh = hh["imp_3p"] - hh["exp_3p"]
                used_kwh = hh["imp_net"] + used_gen_kwh + used_3p_kwh
                vals.append(str(round(used_kwh, 2)))
            if vals is not None:
                writer.writerow(vals)
    except BaseException:
        msg = traceback.format_exc()
        sys.stderr.write(msg)
        f.write(msg)
    finally:
        if sess is not None:
            sess.close()
        if f is not None:
            f.close()
            os.rename(running_name, finished_name)


def do_get(sess):
    start_date = req_date("start", "day")
    finish_year = req_int("finish_year")
    finish_month = req_int("finish_month")
    finish_day = req_int("finish_day")
    finish_date_ct = ct_datetime(finish_year, finish_month, finish_day, 23, 30)
    finish_date = to_utc(finish_date_ct)

    finish_date_str = finish_date_ct.strftime("%Y%m%d%H%M")
    if "site_id" in request.values:
        site_id = req_int("site_id")
        file_name = "sites_hh_data_" + str(site_id) + "_" + finish_date_str + ".csv"
    else:
        site_id = None
        file_name = "supplies_hh_data_" + finish_date_str + ".zip"

    content = none_content if site_id is None else site_content
    args = (site_id, start_date, finish_date, g.user, file_name)
    threading.Thread(target=content, args=args).start()
    return chellow_redirect("/downloads", 303)
