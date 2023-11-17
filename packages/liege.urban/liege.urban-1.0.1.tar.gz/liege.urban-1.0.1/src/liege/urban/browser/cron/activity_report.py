# -*- coding: utf-8 -*-

from datetime import date

from liege.urban.browser.activity_report import do_export

from plone import api
from plone.app.async.interfaces import IAsyncService

from Products.Five import BrowserView
from Products.urban.config import URBAN_TYPES

from zope.component import getUtility


class MonthlyActivityReport(BrowserView):
    """
    """

    query = {
        'date_index': 'created',
        'start_date': date(2000, 1, 1),
        'end_date': date(date.today().year, date.today().month, date.today().day),
        'licence_type': set(
            URBAN_TYPES
        ),
    }

    def __call__(self):
        _async = getUtility(IAsyncService)
        job = _async.queueJob(do_export, self.context, self.query, 'monthly_activity_report')


class GetMonthlyActivityReportResult(BrowserView):
    """
    """

    def __call__(self):
        response = self.context.REQUEST.RESPONSE
        response.setHeader('Content-type', 'application/zip')
        response.setHeader('Content-disposition', 'monthly_activity_report.zip')
        json_export = open('monthly_activity_report.zip', 'rb')
        raw_export = json_export.read()
        response.setBody(raw_export)
        json_export.close()
        return raw_export
