from model.model import MattingRefine
import torch
from torchvision.transforms.functional import to_tensor, to_pil_image
import cv2
from PIL import Image

def main(org_img):
    src = Image.open(org_img)
    w,h = src.size
    if w % 4 != 0:
        w = w + (4 - w % 4)
    if h % 4 != 0:
        h = h + (4 - h % 4)
    src = src.resize((w, h), Image.ANTIALIAS)
    img_deal = src.convert('RGB')
    img_deal.save(org_img)
    img = cv2.imread(org_img)
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    b, g, r = img2[15, 15]
    bgr = Image.new("RGB",(w,h),(b,g,r))
    src = to_tensor(src).unsqueeze(0)
    bgr = to_tensor(bgr).unsqueeze(0)
    device = torch.device('cpu')
    precision = torch.float32
    model = MattingRefine(backbone='resnet101',
                          backbone_scale=0.25,
                          refine_mode='sampling',
                          refine_sample_pixels=80_000)

    model.load_state_dict(torch.load('model\pytorch_resnet101.pth'))
    model = model.eval().to(precision).to(device)
    pha, fgr = model(src, bgr)[:2]
    to_pil_image(pha[0].cpu()).save('pha.png')



    def erode_dilate(mask, size=(17, 17), smooth=True):
        if smooth:
            size = (size[0] - 4, size[1] - 4)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, size)

        dilated = cv2.dilate(mask, kernel, iterations=1)
        if smooth:
            dilated[(dilated > 15)] = 255
            dilated[(dilated <= 15)] = 0
        else:
            dilated[(dilated > 0)] = 255
        eroded = cv2.erode(mask, kernel, iterations=1)
        if smooth:
            eroded[(eroded < 255)] = 0
            eroded[(eroded >= 255)] = 255
        else:
            eroded[(eroded < 255)] = 0
        res = dilated.copy()
        res[((dilated == 255) & (eroded == 0))] = 128
        return res
    msk = cv2.imread('pha.png')
    res = erode_dilate(msk)
    cv2.imwrite('trimap.png', res)




