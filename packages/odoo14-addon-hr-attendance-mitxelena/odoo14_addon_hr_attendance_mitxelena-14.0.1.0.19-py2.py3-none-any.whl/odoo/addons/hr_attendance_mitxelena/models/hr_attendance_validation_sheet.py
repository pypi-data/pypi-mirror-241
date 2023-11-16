from datetime import timedelta

from odoo import api, fields, models, _


class HrAttendanceValidationSheet(models.Model):
    _inherit = "hr.attendance.validation.sheet"

    def name_get(self):
        results = []
        for rec in self:
            results.append(
                (
                    rec.id,
                    _("[%s] %s - %s")
                    % (
                        rec.date_from.strftime("%Y"),
                        rec.date_from.strftime("%B"),
                        rec.employee_id.name,
                    ),
                )
            )
        return results

    def _default_from_date(self):
        """returns the fist day of the past month"""
        today = fields.Date.today()
        month = today.month - 1 if today.month > 1 else 12
        return today.replace(day=1, month=month)

    def _default_to_date(self):
        """returns last day of previous month"""
        today = fields.Date.today()
        return today.replace(day=1) - timedelta(days=1)

    date_from = fields.Date(
        string="Date from",
        required=True,
        default=_default_from_date,
    )

    date_to = fields.Date(
        string="Date to",
        required=True,
        default=_default_to_date,
    )

    @api.onchange("employee_id")
    def _default_calendar_id(self):
        """returns the calendar of the employee for the month of the validation sheet"""
        if not self.employee_id:
            return
        month = self._default_from_date().month
        year = self._default_from_date().year
        cal = self.employee_id.resource_calendar_id.hours_per_day
        external_id = f"hr_attendance_mitxelena.calendar_{year}_{month}_{cal}h"
        cal_id = self.env["ir.model.data"].xmlid_to_res_id(external_id)
        calendar_external_id = self.env["resource.calendar"].search(
            [("id", "=", cal_id)]
        )
        return {'value': {'calendar_id': calendar_external_id.id}}
    
    calendar_id = fields.Many2one(
        "resource.calendar",
        string="Calendar",
        required=True,
        related="",
        default=_default_calendar_id,
    )

    employee_id = fields.Many2one(
        "hr.employee",
        string="Employee",
        required=True,
        ondelete="cascade",
        index=True,
    )

    mother_calendar_id = fields.Many2one(
        "resource.calendar",
        string="Resource Calendar",
        related="employee_id.mother_calendar_id",
        readonly=True,
        store=False,
    )
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company,
    )

    theoretical_hours = fields.Float(
        string="Theoretical (hours)",
        related="calendar_id.total_hours",
        help="Theoretical calendar hours to spend by week.",
    )

    attendance_hours = fields.Float(
        "Attendance (hours)",
        compute="_compute_attendances_hours",
        help="Compute number of attendance lines not marked as overtime",
    )
    attendance_total_hours = fields.Float(
        "Total Attendance (hours)",
        compute="_compute_attendances_hours",
        help="Validated attendances. Sum attendance and due overtime lines.",
    )
    overtime_due_hours = fields.Float(
        "Overtime due (hours)",
        compute="_compute_attendances_hours",
        help="Compute number of attendance lines marked as overtime which are marked as due",
    )
    overtime_not_due_hours = fields.Float(
        "Overtime not due (hours)",
        compute="_compute_attendances_hours",
        help="Compute number of attendance lines marked as overtime which are not due",
    )

    # This function will need to be overriden in order to compute the leave hours
    # in case the leave is not recorded by hours or half days, as it recomputes
    # the hours based on the calendar attendances and week days.
    @api.depends("leave_ids")
    def _compute_leaves(self):
        for record in self:
            leave_hours = 0
            for leave in record.leave_ids:
                if leave.request_unit_half or leave.request_unit_hours:
                    # we assume time off is recorded by hours
                    leave_hours += leave.number_of_hours_display
                else:
                    current_date = max(leave.request_date_from, record.date_from)
                    date_to = min(
                        leave.request_date_to or leave.request_date_from, record.date_to
                    )
                    while current_date <= date_to:
                        # we sum the hours per day from calendar if it is a working day
                        # TODO: check how to handle when it is a time off day
                        # (holiday or global time off)
                        if current_date.weekday() < 5:
                            leave_hours += record.calendar_id.hours_per_day
                        current_date += timedelta(days=1)

            record.leave_hours = leave_hours

    # This function will need to be overriden in order to compute the
    # attendance hours using the extra_time_with_factor.
    @api.depends("attendance_ids", "attendance_ids.is_overtime")
    def _compute_attendances_hours(self):
        for record in self:
            record.attendance_hours = sum(
                record.attendance_ids.filtered(lambda att: not att.is_overtime).mapped(
                    "worked_hours"
                )
            )
            record.overtime_due_hours = sum(
                record.attendance_ids.filtered(
                    lambda att: att.is_overtime and att.is_overtime_due
                ).mapped("extra_time_with_factor")
            )
            record.overtime_not_due_hours = sum(
                record.attendance_ids.filtered(
                    lambda att: att.is_overtime and not att.is_overtime_due
                ).mapped("extra_time_with_factor")
            )
            record.attendance_total_hours = sum(
                record.attendance_due_ids.filtered(
                    lambda att: not att.is_relevo
                ).mapped("extra_time_with_factor")
                + record.attendance_ids.filtered(lambda att: att.is_relevo).mapped(
                    "worked_hours"
                )
            )
