# 以系统开发者人名作为key值
projects_view_name_dict = {
    "chen_1": "生产场景中异常事件的探测",
    "chen_2": "生产流程的多维分析与可视化",
    "li": "生产线上传感器采集、分析与显示",
    "yv_1": "日志数据的度量和自动抽取",
    "yv_2": "复杂生产业务流程建模、挖掘与优化",
    "wang": "生产操作行为的自动识别",
    "pan": "生产场景中目标的自动检测",
    "ding": "AGV运载车实时状态监控系统",
}

# 系统图标的位置
projects_icon_position = ["wang", "pan", "yv_1", "li", "yv_2", "chen_1", "chen_2", "ding"]

label_image_paths_dict = {
    "chen_1": "images/intrusion.jpg",
    "chen_2": "images/data_analysis.jpg",
    "li": "images/sensors.jpg",
    "yv_1": "images/opc_start.png",
    "yv_2": "images/cps_start.png",
    "wang": "images/xiowork.jpg",
    "pan": "images/robam.png",
    "ding": "images/agv.jpg",
    # "yue": "images/houban_oee.png",
}

# 系统启动命令 (eg. python.exe main.py)
projects_command_dict = {
    "chen_1": "D:/Anaconda3/envs/xio/python.exe E:/projects-summary/xio-intrusion-detection/run_forever.py",
    "chen_2": "D:/Anaconda3/envs/xio/python.exe E:/projects-summary/data-multidimensional-analysis/main.py",
    "li": "D:/Anaconda3/envs/xio/python.exe E:/projects-summary/QT/Main.py",
    "yv_1": "D:/Anaconda3/envs/xio/python.exe E:/projects-summary/xio/opc_start.py",
    "yv_2": "D:/Anaconda3/envs/xio/python.exe E:/projects-summary/xio/cps_start.py",
    "wang": "D:/Anaconda3/envs/legacy/python.exe E:/projects-summary/xiaowork/xio_all.py",  # PyQt4 的环境
    "pan": "D:/Anaconda3/envs/xio/python.exe E:/projects-summary/component-detection-camera2/gui_main.py",
    "ding": "D:/Anaconda3/envs/xio/python.exe E:/projects-summary/agv2/Run.py",
    # "yue": "D:/Anaconda3/envs/legacy/python.exe E:/projects-summary/xioLift/xio_all.py",  # PyQt4 的环境
}

projects_cwd_dict = {
    "chen_1": "E:/projects-summary/xio-intrusion-detection",
    "chen_2": "E:/projects-summary/data-multidimensional-analysis",
    "li": "E:/projects-summary/QT",
    "yv_1": "E:/projects-summary/xio",
    "yv_2": "E:/projects-summary/xio",
    "wang": "E:/projects-summary/xiaowork",
    "pan": "E:/projects-summary/component-detection-camera2",
    "ding": "E:/projects-summary/agv2",
    # "yue": "E:/projects-summary/xioLift",
}
