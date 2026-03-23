from odoo import models, fields, api


class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    _rec_name = 'ho_ten'

    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ho_ten = fields.Char("Họ và tên", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    cccd = fields.Char("Căn cước công dân")
    bhxh = fields.Char("Mã số BHXH")
    luong = fields.Float("Lương cơ bản")
    
    phong_ban_ids = fields.Many2many(
        comodel_name='phong_ban',
        string='Phòng ban'
    )
    chung_chi_ids = fields.One2many(
        comodel_name='chung_chi_bang_cap',
        inverse_name='nhan_vien_id',
        string='Chứng chỉ'
    )