from django.db import models

# Create your models here.


"""class Notices(models.Model):
    id = models.AutoField('记录编号', primary_key=True)
    title = models.CharField('通知标题', max_length=32, null=False)
    detail = models.CharField('通知详情', max_length=32, null=False)
    createTime = models.CharField('通知时间', db_column='create_time', max_length=19)

    class Meta:
        db_table = 'notices'
"""


# 测试数据接口
class users(models.Model):
    time = models.DateTimeField(verbose_name="时间")
    user = models.CharField(verbose_name="用户名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=32)
    age = models.CharField(verbose_name="年龄", max_length=16)
    sexy = models.CharField(verbose_name="性别", max_length=8)
    level = models.IntegerField(verbose_name="级别")


# 造型设备参数
class zaoxing_parameter(models.Model):
    time = models.DateTimeField(verbose_name="时间")
    hunshaji_state = models.BooleanField(verbose_name="混砂机运行状态")
    environment_temperature = models.FloatField(verbose_name="环境温度", max_length=8)
    xingsha_temperature = models.DecimalField(verbose_name="型砂温度", max_digits=8, decimal_places=2)
    gansha_flow_rate = models.FloatField(verbose_name="干砂流量", max_length=8)
    shuzhi_flow_rate = models.FloatField(verbose_name="树脂流量", max_length=8)
    guhuaji1_flow_rate = models.FloatField(verbose_name="固化剂1流量", max_length=8)
    guhuaji2_flow_rate = models.FloatField(verbose_name="固化剂2流量", max_length=8)
    zhenshitai_state = models.BooleanField(verbose_name="振实台运行状态")
    amplitude = models.FloatField(verbose_name="振幅", max_length=8)
    reverse_proportional_valve_signal = models.FloatField(verbose_name="翻转比例阀信号", max_length=8)
    hexiangji_state = models.BooleanField(verbose_name="起模流涂合箱机运行状态")
    oil_temperature = models.FloatField(verbose_name="液压站油温", max_length=8)
    curing_time = models.FloatField(verbose_name="固化时间", max_length=8)
    dry_temperature = models.FloatField(verbose_name="表干温度", max_length=8)
    drying_time = models.FloatField(verbose_name="表干时间", max_length=8)


# 熔炼设备参数
class ronglian_parameter(models.Model):
    time = models.DateTimeField(verbose_name="时间")
    zhuluti_state = models.BooleanField(verbose_name="主炉体运行状态")
    gas_flow = models.FloatField(verbose_name="天然气流量", max_length=8)
    gas_pressure = models.FloatField(verbose_name="天然气压力", max_length=8)
    fan_pressure = models.FloatField(verbose_name="风机压力", max_length=8)
    furnace_temperature = models.FloatField(verbose_name="炉膛温度", max_length=8)
    liquid_temperature = models.FloatField(verbose_name="溶液温度", max_length=8)
    melt_composition = models.CharField(verbose_name="熔体成分", max_length=16)
    hydrogen_content = models.FloatField(verbose_name="氢含量", max_length=8)
    electromagnetic_stirring_current = models.FloatField(verbose_name="电磁搅拌电流", max_length=8)
    argon_flow = models.FloatField(verbose_name="氩气流量", max_length=8)
    zhuanglu_system_state = models.BooleanField(verbose_name="装炉系统运行状态")
    pure_aluminum_amount = models.FloatField(verbose_name="纯铝加入量", max_length=8)
    alloying_quantity = models.FloatField(verbose_name="中间合金长条锭加入量", max_length=8)
    pure_aluminium_allowance = models.FloatField(verbose_name="纯铝余量", max_length=8)
    alloy_allowance = models.FloatField(verbose_name="中间合金长条锭余量", max_length=8)
    jiliao_system_state = models.BooleanField(verbose_name="给料系统运行状态")
    theory_replenishment_weight = models.FloatField(verbose_name="中间合金理论补给重量", max_length=8)
    actual_replenishment_weight = models.FloatField(verbose_name="中间合金实际补给重量", max_length=8)
    refining_temperature = models.FloatField(verbose_name="精炼温度", max_length=8)
    refining_agent_amount = models.FloatField(verbose_name="精炼剂用量", max_length=8)
    duoxing_gas_flow = models.FloatField(verbose_name="惰性气体流量", max_length=8)
    refining_time = models.FloatField(verbose_name="精炼时间", max_length=8)


# 铸造设备参数
class zhuzao_parameter(models.Model):
    time = models.DateTimeField(verbose_name="时间")
    zhuzaoji_state = models.BooleanField(verbose_name="铸造机运行状态")
    jiaozhu_temperature = models.FloatField(verbose_name="浇注熔体温度", max_length=8)
    tank_pressure_on = models.FloatField(verbose_name="上罐压力", max_length=8)
    tank_pressure_off = models.FloatField(verbose_name="下罐压力", max_length=8)
    chongxing_pressure = models.FloatField(verbose_name="充型压力", max_length=8)
    chongxing_time = models.FloatField(verbose_name="充型时间", max_length=8)
    baoya_pressure = models.FloatField(verbose_name="保压压力", max_length=8)
    baoya_time = models.FloatField(verbose_name="凝固保压时间", max_length=8)
    magnetic_field_current = models.FloatField(verbose_name="磁场电流", max_length=8)
    dianzhen_temperature = models.FloatField(verbose_name="点阵温度", max_length=8)
    gongzuocanglongmen_state = models.BooleanField(verbose_name="工作舱龙门运行状态")
    duogongnenglongmen_state = models.BooleanField(verbose_name="多功能龙门运行状态")
    manipulator_state = models.BooleanField(verbose_name="升液管机械手运行状态")


# 检测设备参数
class jiance_parameter(models.Model):
    time = models.DateTimeField(verbose_name="时间")
    PLC_state = models.BooleanField(verbose_name="PLC运行状态")
    touch_screen_state = models.BooleanField(verbose_name="触摸屏运行状态")
    flat_panel_detector_state = models.BooleanField(verbose_name="平板探测器运行状态")
    shexianyuan_state = models.BooleanField(verbose_name="射线源运行状态")
    robot_state = models.BooleanField(verbose_name="机器人运行状态")
    industrial_state = models.BooleanField(verbose_name="工控机运行状态")
    camera1_state = models.BooleanField(verbose_name="监控摄像头1运行状态")
    camera2_state = models.BooleanField(verbose_name="监控摄像头2运行状态")
    current_feedback = models.FloatField(verbose_name="电流反馈", max_length=8)
    voltage_feedback = models.FloatField(verbose_name="电压反馈", max_length=8)


# 手动输入参数
class manual_input(models.Model):
    time = models.DateTimeField(verbose_name="时间")
    zaoxing_model_information = models.CharField(verbose_name="造型模型信息", max_length=16)
    vibrational_frequency = models.FloatField(verbose_name="振动频率", max_length=8)
    alloy_designation = models.CharField(verbose_name="合金牌号", max_length=16)
    total_melt_amount = models.FloatField(verbose_name="总熔化量", max_length=8)
    small_allowance = models.FloatField(verbose_name="中间合金小块锭余量", max_length=8)
    zhuzao_model_information = models.CharField(verbose_name="铸造模型信息", max_length=16)


