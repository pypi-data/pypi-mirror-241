import datetime

from odoo import _, api, models
from odoo.exceptions import UserError, ValidationError


class ParticularReport(models.AbstractModel):
    _name = "report.hr_attendance_mitxelena.report_hr_attendance_template"

    # def _get_report_values(self, docids, data=None):
    #     # get the report action back as we will need its data
    #     # report = self.env['ir.actions.report']._get_report_from_name('attendance_report.report_hr_attendance_template')  # noqa
    #     # get the records selected for this rendering of the report
    #     # obj = self.env[report.model].browse(data['docids'])

    #     return {
    #         "docids": data['docids'],
    #         "doc_model": "hr.attendance",
    #     }

    # assistance_report = self.env['ir.actions.report']._get_report_from_name('hr_holidays.report_hr_attendance_template')  # noqa
    # assistances = self.env['hr.assistance'].browse(self.ids)

    @api.model
    def _get_report_values(self, docids, data=None):

        if not data.get("form_data"):
            raise UserError(
                _("Form content is missing, this report cannot be printed.")
            )

        attendance_validation_sheet = self.env["hr.attendance.validation.sheet"].browse(data["form_data"]["attendance_sheet_id"][0])

        return {
            "doc_ids": [attendance_validation_sheet.id],
            "doc_model": "hr.attendance.validation.sheet",
            "docs": attendance_validation_sheet,
            "data": data,
        }
