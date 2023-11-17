#!/usr/bin/env python
#-*- coding: utf-8 -*-
#PROJECT_NAME: E:\code\easyofd\easyofd\draw
#CREATE_TIME: 2023-08-10 
#E_MAIL: renoyuan@foxmail.com
#AUTHOR: reno 
#NOTE:  绘制pdf
import os
import re
import traceback
import base64
import logging
import copy
import json
from PIL import Image as PILImage
from io import BytesIO

from reportlab import platypus
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm,inch
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import fonts as reportlab_fonts

from easyofd.draw.font_tools import FontTool
from loguru import logger

# print(reportlab_fonts)
class DrawPDF():
    """
    ofd 解析结果 绘制pdf
    OP ofd 单位转换
    """
    def __init__(self,data,*args, **kwargs):
        assert data,"未输入ofd解析结果"
        self.data = data
        self.author = "renoyuan"
        self.OP = 200/25.4
        self.pdf_uuid_name=self.data[0]["pdf_name"]
        self.pdf_io = BytesIO() 
        self.SupportImgType = ("JPG","IPEG","PNG")
        self.init_font = "宋体"
        self.font_tool = FontTool()
    
   
    
    def draw_lines(my_canvas):
        """
        draw_line
        """
        my_canvas.setLineWidth(.3)
        
        start_y = 710
        my_canvas.line(30, start_y, 580, start_y)
    
        for x in range(10):
            start_y -= 10
            my_canvas.line(30, start_y, 580, start_y)
    
 

    def gen_empty_pdf(self):
        """
        """
        c = canvas.Canvas(self.pdf_io)
        c.setPageSize(A4)
        c.setFont(self.init_font, 20)
        c.drawString(0,210,"ofd 格式错误,不支持解析", mode=1  )
        c.save()
    
    # 单个字符偏移量计算
    def cmp_offset(self,pos,offset,DeltaRule,text,resize=1)->list:
        """
        pos 文本框x|y 坐标 
        offset 第一个字符的X|Y 
        DeltaRule 偏移量规则
        resize 字符坐标缩放
        返回 x|y  字符位置list 
        """

        char_pos = float(pos if pos else 0 ) + float(offset if offset else 0 )* resize
        pos_list = []
        pos_list.append(char_pos) # 放入第一个字符
        offsets = [i for i in DeltaRule.split(" ")]

        if "g" in   DeltaRule:  # g 代表多个元素
            g_no = None
            for _no, offset_i in enumerate(offsets) :
            
                if offset_i == "g":
                    g_no = _no
                    for j in range(int(offsets[(g_no+1)])):
                        char_pos += float(offsets[(g_no+2)]) 
                        pos_list.append(char_pos)
                    
                elif offset_i != "g" :
                    if g_no == None:
                        char_pos += float(offset_i) * resize
                        pos_list.append(char_pos)
                    elif  (int(_no) > int(g_no+2)) and g_no!=None:
                      
                        char_pos += float(offset_i)  * resize
                        pos_list.append(char_pos)
                    
        elif not DeltaRule: # 没有字符偏移量 一般单字符
            pos_list = []
            for i in range(len(text)):
                pos_list.append(char_pos)
        else: # 有字符偏移量
            for i in offsets:
                if not i:
                    char_pos += 0
                else:
                    char_pos += float(i)  * resize
                pos_list.append(char_pos)
                
        return pos_list
        
                       
    def draw_pdf(self):
       
        c = canvas.Canvas(self.pdf_io)
        c.setAuthor(self.author)

        for doc_id,doc in enumerate(self.data,start=1)  :
            fonts = doc.get("fonts")
            images = doc.get("images")
            page_size= doc.get("page_size")
            
            # 注册字体
            for font_id,font_v in fonts.items():    
                file_name = font_v.get("FontFile")
                font_b64 = font_v.get("font_b64")
                if font_b64:
                    self.font_tool.register_font(os.path.split(file_name)[1],font_v.get("@FontName"),font_b64)
            # text_write = [] 
            for page_id,page in doc.get("page_info").items():     
                text_list = page.get("text_list")
                img_list = page.get("img_list")
                # print("img_list",img_list)
              
                c.setPageSize((page_size[2]*self.OP, page_size[3]*self.OP))

                # 写入图片
                for img_d in img_list:
                    image = images.get(img_d["ResourceID"])
                    
                    if not image or image.get("suffix").upper() not in self.SupportImgType:
                        continue
                    
                    imgbyte = base64.b64decode(image.get('imgb64'))
                    img = PILImage.open(BytesIO(imgbyte))
                    imgReade  = ImageReader(img)
                    CTM = img_d.get('CTM')
                    x_offset = 0
                    y_offset = 0
                    wrap_pos = image.get("wrap_pos")
                    x = (img_d.get('pos')[0]+x_offset)*self.OP
                    y = (page_size[3] - (img_d.get('pos')[1]+y_offset))*self.OP
                    if wrap_pos:
                        x = x+(wrap_pos[0]*self.OP)
                        y = y-(wrap_pos[1]*self.OP)
                    w =   img_d.get('pos')[2]*self.OP
                    h =  -img_d.get('pos')[3]*self.OP
                    c.drawImage(imgReade,x,y ,w, h, 'auto')

                # 写入文本
                # text_list_cp =  copy.deepcopy(text_list)
                # text_list_new = self.text_seria(text_list_cp)
                for line_dict in text_list:
                    # TODO 写入前对于正文内容整体序列化一次 方便 查看最后输入值 对于最终 格式先
                    text = line_dict.get("text")
                    font_info = fonts.get(line_dict.get("font"),{})
                    if font_info:
                        font_name = font_info.get("FontName","")
                    else:
                        font_name = self.init_font
                        
                    # TODO 判断是否通用已有字体 否则匹配相近字体使用
                    if font_name not in self.font_tool.FONTS:
                        font_name = self.font_tool.FONTS[0]
                    
                    font=font_name
                    # if font not in FONT: #  KeyError: 'SWDRSO+KaiTi-KaiTi-0'
                        
                    c.setFont(font, line_dict["size"]*self.OP)
                    # 原点在页面的左下角 
                    color = line_dict.get("color",[0,0,0])
                    c.setFillColorRGB(int(color[0])/255,int(color[1])/255, int(color[2])/255)
                    c.setStrokeColorRGB(int(color[0])/255,int(color[1])/255, int(color[2])/255)
                    
                    DeltaX = line_dict.get("DeltaX","")
                    DeltaY = line_dict.get("DeltaY","")
                    X = line_dict.get("X","")
                    Y = line_dict.get("Y","")
                    CTM = line_dict.get("CTM","") # 因为ofd 的傻逼 增加这个字符缩放
                    resizeX =1
                    resizeY =1
                    if CTM :
                        resizeX = float(CTM.split(" ")[0])
                        resizeY = float(CTM.split(" ")[3])
                
                    x_list = self.cmp_offset(line_dict.get("pos")[0],X,DeltaX,text,resizeX)
                    y_list = self.cmp_offset(line_dict.get("pos")[1],Y,DeltaY,text,resizeY)
                    

                    # if line_dict.get("Glyphs_d") and  FontFilePath.get(line_dict["font"])  and font_f not in FONTS:
                    if False: # 对于自定义字体 写入字形 drawPath 性能差暂时作废
                        Glyphs = [int(i) for i in line_dict.get("Glyphs_d").get("Glyphs").split(" ")]
                        for idx,Glyph_id in enumerate(Glyphs):
                            _cahr_x= float(x_list[idx])*self.OP
                            _cahr_y= (float(page_size[3])-(float(y_list[idx])))*self.OP
                            imageFile = draw_Glyph( FontFilePath.get(line_dict["font"]), Glyph_id,text[idx])
                            
                            # font_img_info.append((FontFilePath.get(line_dict["font"]), Glyph_id,text[idx],_cahr_x,_cahr_y,-line_dict["size"]*Op*2,line_dict["size"]*Op*2))
                            c.drawImage(imageFile,_cahr_x,_cahr_y,-line_dict["size"]*self.OP*2,line_dict["size"]*self.OP*2  )
                            
                    else:
                        if len(text) > len(x_list) or len(text) > len(y_list) :
                            text = re.sub("[^\u4e00-\u9fa5]","",text)  
                        try:
                            # 按行写入  最后一个字符y  算出来大于 y轴  最后一个字符x  算出来大于 x轴 
                            if y_list[-1]*self.OP > page_size[3]*self.OP or x_list[-1]*self.OP >page_size[2]*self.OP or x_list[-1]<0 or y_list[-1]<0 :
                                # print("line wtite")
                                x_p = abs(float(X) )*self.OP
                                y_p = abs(float(page_size[3])-(float(Y)))*self.OP
                                c.drawString(x_p,  y_p, text, mode=0) # mode=3 文字不可见 0可見
                           
                                # text_write.append((x_p,  y_p, text))
                            # 按字符写入
                            else:
                                for cahr_id, _cahr_ in enumerate(text) :
                                    # print("char wtite")
                                    _cahr_x= float(x_list[cahr_id])*self.OP
                                    _cahr_y= (float(page_size[3])-(float(y_list[cahr_id])))*self.OP                                        
                                    c.drawString( _cahr_x,  _cahr_y, _cahr_, mode=0) # mode=3 文字不可见 0可見
                                
                                    # text_write.append((_cahr_x,  _cahr_y, _cahr_))
                            
                        except Exception as e:
                            logger.error(f"{e}")
                            traceback.print_exc()
            
                if page_id != len(doc.get("page_info"))-1  and doc_id != len(self.data): 
                    c.showPage()  
            # json.dump(text_write,open("text_write.json","w",encoding="utf-8"),ensure_ascii=False)
        c.save()
        
    def __call__(self):
        try:
            self.draw_pdf()
            pdfbytes  = self.pdf_io.getvalue()
        except Exception as e:
            logger.error(f"{e}")
            logger.error(f"ofd解析失败")
            traceback.print_exc()
            self.gen_empty_pdf()
            pdfbytes  = self.pdf_io.getvalue()
        return pdfbytes
