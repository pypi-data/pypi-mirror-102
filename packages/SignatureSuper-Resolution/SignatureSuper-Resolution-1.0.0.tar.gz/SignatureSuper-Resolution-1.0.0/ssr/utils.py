from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
def draw_img_nop(data, dt):
    """
    :param data: pandas.DataFrame, [X, Y, P, T]
    :param dt: 设定时间间隔异常的值，画图会突出显示
    :return:
    """
    # 移动文字到左上角
    sign_data = data.copy()
    sign_data['X'] = sign_data['X'] - (sign_data['X'].min()) + 10
    sign_data['Y'] = sign_data['Y'] - (sign_data['Y'].min()) + 10
    w, h = int(sign_data["X"].max()) + 20, int(sign_data["Y"].max()) + 20

    img = Image.new('RGB', size=(int(w), int(h)), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    x_seq, y_seq, p_seq = sign_data["X"].values, sign_data["Y"].values, sign_data["P"].values
    strange = sign_data["T"].diff()[sign_data["T"].diff() > dt].index.tolist()

    for i in range(len(sign_data) - 1):
        color = "white" if i + 1 not in strange else "green"
        draw.line((x_seq[i], y_seq[i], x_seq[i + 1], y_seq[i + 1]), fill=color, width=50)

    plt.figure(dpi=100, figsize=(24, 12))
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img)


def draw_img(data, is_show=False):
    """根据原数据(txt数据)绘制并保存图片


    :param data:  pandas.DataFrame,文件名 或者 签名数据
    :param save_basepath: str,保存的基路径,默认为None，表示不保存
    :param is_show: bool,是否展示出来，默认为False
    :param is_draw_keypoint: bool,是否绘制关键点，默认为False
    :param is_resize: 是否进行缩放
    :param size: (int,int),缩放后大小
    :return: ~PIL.Image.Image 签字图像
    """
    """判断数据"""
    if isinstance(data, pd.DataFrame):
        sign_data = data.copy()
    else:
        raise ValueError('输入类型错误！')

    """画图"""
    # 移动文字到左上角
    sign_data['X'] = sign_data['X'] - (sign_data['X'].min()) + 10
    sign_data['Y'] = sign_data['Y'] - (sign_data['Y'].min()) + 10
    w, h = int(sign_data["X"].max()) + 20, int(sign_data["Y"].max()) + 20

    nw, nh = w, h
    img = Image.new('RGB', size=(int(nw), int(nh)), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    # base_w = 0.005
    base_w = 0.01
    x_seq, y_seq, p_seq = sign_data["X"].values, sign_data["Y"].values, sign_data["P"].values

    p_seq = (p_seq - min(p_seq)) / (max(p_seq) - min(p_seq))  # 归一化，压力百分比
    for i in range(len(sign_data) - 1):
        if p_seq[i] <= 0: continue
        w = int(p_seq[i] * base_w * nw) if p_seq[i] > 0 else 3  # 增加压力信息 按图像比例设置宽度
        draw.line((x_seq[i], y_seq[i], x_seq[i + 1], y_seq[i + 1]), fill='white', width=w)

    """图片展示"""
    if is_show:
        plt.figure(dpi=50, figsize=(12, 6))
        plt.imshow(img)
        plt.xticks([])
        plt.yticks([])
        plt.show()
    plt.close()

    return img.convert('L')

def speed_cmp(d1 ,d2):
    """
    :param d1: pd.DataFrame [X, Y, P, T]
    :param d2: pd.DataFrame [X, Y, P, T]
    :return:
    对两个签字序列数据进行对比，第一列为x方向速度，第二列为y方向速度，第三列为压力对比
    """
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    t1, t2 = int(d1["T"].diff().mean()), int(d2["T"].diff().mean())
    for i, data in enumerate([d1, d2]):
        t = t2 if i % 2 else t1
        axes[i][0].plot(range(len(data)), data['X'].diff() / t)
        axes[i][1].plot(range(len(data)), data['Y'].diff() / t)
        axes[i][2].plot(range(len(data)), data['P'])
    plt.show()

def down_sample(data, down_pps = 60):
    """
    after data clean
    data: pd.DataFrame，[X,Y,P,T] data["T"]非间隔，从0开始
    down_pps: 默认下采样报点率60
    return lr_data: 下采样数据
           pps: 原报点率
           down_pps: 返回数据报点率
    """
    pps = 1000 / (data["T"].diff().mean())
    lr_data = data[::round(pps // down_pps)]

    return lr_data, pps, down_pps

