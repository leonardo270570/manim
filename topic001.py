from manim import *
from flesmynmanim import *
from itertools import cycle

# Portrait Video
# manim -pqh topic001.py Topic001 -r "1080,1920"
# is_portrait = True

# Landscape Video
# manim -pqh topic001.py Topic001
# is_portrait = False

# Topic : x1^n + x2^n in terms of x1 + x2 and x1.x2

class Topic001(ZoomedScene):
    def construct(self):
        # variables related to the topic
        n_order = 6
        iteration_count = n_order // 2 + 1  # generate the detail elements

        # define the font size factor, including latex size
        m_fontname = 'LM Roman 10'
        m_scalefactor = 1.75 #you just need to change this and will impact to font size
        m_fontsize = 36 * m_scalefactor
        m_adjustmentfont = 0.065 #adjust for font position vertically
        is_portrait = True #true for portrait, added -r "1080,1920"
        m_option = 1 #create 1 = video, 2 = picture, 3 = subtile 

        # define logo and put in the center of the page
        #if m_option != 1 : 
        img_logo_CE = SVGMobject(file_name="images/fm-abs.svg",
                                fill_opacity=.5, stroke_opacity=0,
                                fill_color=GREY_C, stroke_color=GREY_C)
        img_background = ImageMobject("images/bg6.png").scale(3.4)
        self.add(img_background)

        # for music notes
        m_musicnotes = []
        with open('music001.txt') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                m_musicnotes.append(float(line[-5:]))
                #print(float(line[-5:]))

        f.close()

        # create subtitile file
        #if m_option == 3 : 
        f = open("topic001.txt", "a")
        f.write("Subtile topic 001")
        f.write("\n")

        # the list of the formulas and text
        quiztext = []
        # 0-5
        quiztext.append(Text("Express", font=m_fontname,
                             font_size=m_fontsize))
        quiztext.append(
            MathTex("x_{1}^"+str(n_order)+"+x_{2}^"+str(n_order)).scale(m_scalefactor))
        quiztext.append(Text("in terms of",
                             font=m_fontname, font_size=m_fontsize))
        quiztext.append(MathTex("x_{1}+x_{2}").scale(m_scalefactor))
        quiztext.append(Text("and", font=m_fontname, font_size=m_fontsize))
        quiztext.append(MathTex(" x_{1}x_{2}").shift(
            7 * DOWN).scale(m_scalefactor))

        # 6-9
        m_baseindex = len(quiztext)
        for k in range(iteration_count + 1):
            if k == 0:
                quiztext.append(MathTex("x_{1}^"+str(n_order)+"+x_{2}^" + str(n_order), "=",
                                        "\\bigcirc", "(x_{1}+x_{2})^", "{" +
                                        str(n_order - 2 * k) + "}",
                                        "(x_{1}x_{2})^", str(k), "+").scale(m_scalefactor))
                quiztext[m_baseindex].shift(8 * UP)  # row base
            elif k >= iteration_count-1:
                quiztext.append(MathTex("\\bigcirc", "(x_{1}+x_{2})^", "{" + str(n_order - 2 * k) + "}",
                                        "(x_{1}x_{2})^", str(k)).scale(m_scalefactor))
                quiztext[k +
                         m_baseindex].next_to(quiztext[k + m_baseindex - 1], DOWN)
                m_setalign = set_align_down(quiztext,
                    [m_baseindex + k, 0, 0], [m_baseindex, 2, 0])
            else:
                quiztext.append(MathTex("\\bigcirc", "(x_{1}+x_{2})^", "{" + str(n_order - 2 * k) + "}",
                                        "(x_{1}x_{2})^", str(k), "+").scale(m_scalefactor))
                quiztext[k +
                         m_baseindex].next_to(quiztext[k + m_baseindex - 1], DOWN)
                m_setalign = set_align_down(quiztext,
                    [m_baseindex + k, 0, 0], [m_baseindex, 2, 0])


        # build table to calculate the multiplied factors
        m_tableindex = len(quiztext) #index for the table

        m_list = []
        m_row = []
        m_colwidth = []
        m_align = ""
        for k in range(n_order + 1):
            m_row.append([])
            m_align = m_align + "c"
            m_colwidth.append(0.4)
            for l in range(n_order + 1):
                if k == l:
                    #if k < iteration_count:
                        m_row[k].append(2 * (-1)**k)
                    #else:
                    #    m_row[k].append("-")
                elif k < l:
                    m_row[k].append("-")
                else:
                    if l == 0:
                        m_row[k].append(1)
                    else:
                        if k + l > n_order:
                            m_row[k].append("-")
                        else:
                            m_row[k].append(m_row[k-1][l] - m_row[k-1][l-1])
            m_list.append(m_row[k])

        quiztext.append(MathTable(m_list, arrange_in_grid_config={"col_alignments": m_align,
            "col_widths": m_colwidth}).shift(3 * DOWN))
        

        m_plusoneindex = len(quiztext) # 6 = 1 + 1 + 1 + 1 + 1 + 1 
        m_plus1 = ""
        for k in range(n_order):
            m_plus1 = m_plus1 + "+" + "1"
        quiztext.append(MathTex(str(n_order),"=", m_plus1[1:]).scale(m_scalefactor).shift(2 * UP))

        for k in range(n_order + 1):
            for l in range(n_order + 1):
                quiztext[m_tableindex].get_entries(
                    (k+1, l+1)).scale(m_scalefactor * 0.9).set_color(BLUE)

        #shows table to get easy to identify the references
        if m_option == 2:
            self.add(quiztext[m_tableindex])

        # set the color of the part text
        quiztext[1][0][0].set_color(BLUE)
        quiztext[3][0][0].set_color(BLUE)
        quiztext[5][0][0].set_color(BLUE)
        quiztext[1][0][4].set_color(BLUE)
        quiztext[3][0][3].set_color(BLUE)
        quiztext[5][0][2].set_color(BLUE)

        # position of the texts
        quiztext[0].shift(4 * LEFT, 1 * UP)
        quiztext[3].shift(3 * LEFT, 0 * UP)  # row 2 base

        for k in [1, 2, 4, 5]:  # next to
            quiztext[k].next_to(quiztext[k-1])

        m_formula = set_align_next(quiztext, [1, 0, 3], [0, 0, 0], m_adjustmentfont) #tex to text
        m_formula = set_align_next(quiztext, [2, 0, 0], [0, 0, 0], 0)
        m_formula = set_align_next(quiztext, [4, 0, 0], [3, 0, 2], m_adjustmentfont) #text to tex
        m_formula = set_align_next(quiztext, [5, 0, 0], [3, 0, 0], 0)

        m_vgroup1 = set_center_row(quiztext, [0, 1, 2])  # centering
        m_vgroup2 = set_center_row(quiztext, [3, 4, 5])  # centering

        # shows all the indices of all element for animation purpose
        for k in range(len(quiztext)):
            for l in range(len(quiztext[k])):
                m_getindex = get_sub_indexes(quiztext[k][l])
                if m_option == 2 :
                    self.add(quiztext[k][l])
                    self.add(m_getindex)  # add all indices of formulas

        # list of animations
        if m_option == 1:
            m_stepinfo = clip_duration(0, m_musicnotes)
            self.play(Create(m_vgroup1), run_time = m_stepinfo[1])

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            self.play(Create(m_vgroup2), run_time = m_stepinfo[1])

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            self.play(m_vgroup1.animate.shift(10 * UP),
                    m_vgroup2.animate.shift(10 * UP), FadeIn(img_logo_CE), run_time = m_stepinfo[1]) #

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            replace(self, quiztext, [[1, 0]], [[6, 0]], m_stepinfo[1]) #move x1^6 to answer

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            fadein(self, quiztext, [6, 1], m_stepinfo[1]) # show =

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            replace(self, quiztext, [[3, 0]], [[6, 3]], m_stepinfo[1]) #move addition

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            self.play(ReplacementTransform(quiztext[6][0][1].copy(), quiztext[6][4]),
                    ReplacementTransform(quiztext[6][0][5].copy(), quiztext[6][4]), run_time = m_stepinfo[1]) #move 6

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            replace(self, quiztext, [[5, 0]], [[6, 5]], m_stepinfo[1]) #move mult

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            fadein(self, quiztext, [6, 6], m_stepinfo[1]) #show 0
            
            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            replace(self, quiztext, [[6, 3],[6, 5]], [[7, 1],[7, 3]], m_stepinfo[1]) #from 6 to 7

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            replace(self, quiztext, [[7, 1],[7, 3]], [[8, 1],[8, 3]], m_stepinfo[1]) #from 7 to 8

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            replace(self, quiztext, [[8, 1],[8, 3]], [[9, 1],[9, 3]], m_stepinfo[1]) #from 8 to 9

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            replace(self, quiztext, [[9, 1],[9, 3]], [[10, 1],[10, 3]], m_stepinfo[1]) #from 9 to 10

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            replace(self, quiztext, [[6, 4], [7, 2], [8, 2], [9, 2]], [[7, 2], [8, 2], [9, 2], [10, 2]], m_stepinfo[1]) #order addition
            
            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            replace(self, quiztext, [[6, 6], [7, 4], [8, 4], [9, 4]], [[7, 4], [8, 4], [9, 4], [10, 4]], m_stepinfo[1]) #order multiply

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            self.play(Create(quiztext[m_plusoneindex][0][0]), run_time = m_stepinfo[1]) #show 6

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            self.play(Create(quiztext[m_plusoneindex][1][0]), run_time = m_stepinfo[1]) #show =

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            self.play(Create(quiztext[m_plusoneindex]), run_time = m_stepinfo[1]) #show 1 + 1

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            self.play(Create(quiztext[m_tableindex]), run_time = m_stepinfo[1])

        #if m_option == 2:
            # copy 1 items into table
            m_source = VGroup()
            for k in range(n_order):
                m_source.add(quiztext[m_plusoneindex][2][2 * k].copy())
    
            m_target = VGroup()
            for k in range(n_order):
                m_target.add(quiztext[m_tableindex][0][(n_order + 1) * (k + 1)])

            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            replace_lagstart(self, quiztext, m_source, m_target, m_stepinfo[1])

            m_var1 = quiztext[m_tableindex].get_entries(
                (n_order+1, 1)).copy().next_to(quiztext[6][3][0], LEFT)
            m_var2 = quiztext[m_tableindex].get_entries(
                (n_order, 2)).copy().next_to(quiztext[7][1][0], LEFT)
            m_var3 = quiztext[m_tableindex].get_entries(
                (n_order-1, 3)).copy().next_to(quiztext[8][1][0], LEFT)
            m_var4 = quiztext[m_tableindex].get_entries(
                (n_order-2, 4)).copy().next_to(quiztext[9][1][0], LEFT)

            #self.play(FadeIn(quiztext[m_tableindex]), run_time=3)
            
            #self.wait(2)

            # self.play(GrowFromCenter(img_logo_CE), run_time=1)
            # self.play(FadeIn(quiztext[1]), run_time=3)
            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            self.play(quiztext[m_tableindex].get_entries(
                (n_order+1, 1)).copy().animate.move_to(m_var1), FadeOut(quiztext[6][2][0]), run_time = m_stepinfo[1])
            
            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            self.play(quiztext[m_tableindex].get_entries(
                (n_order, 2)).copy().animate.move_to(m_var2), FadeOut(quiztext[7][0][0]), run_time = m_stepinfo[1])
            
            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            self.play(quiztext[m_tableindex].get_entries(
                (n_order-1, 3)).copy().animate.move_to(m_var3), FadeOut(quiztext[8][0][0]), run_time = m_stepinfo[1])
            
            m_stepinfo = clip_duration(m_stepinfo[0], m_musicnotes)
            self.play(quiztext[m_tableindex].get_entries(
                (n_order-2, 4)).copy().animate.move_to(m_var4), FadeOut(quiztext[9][0][0]), run_time = m_stepinfo[1])
            
            #print(m_stepinfo[0])
            self.wait(2)

            # transform_index = [
            #     ["f0","f1",2,3,4,"r4"],
            # #  |    |   | | |  |
            # #  v    v   v v v  v
            #     [ 3,   4,  0,1,2, 5]
            # ]
            # self.play(
            #     *[
            #         ReplacementTransform(source[i],target[j])
            #         if type(i) is int else
            #         ReplacementTransform(source[int(i[1:])].copy(),target[j])
            #         if i[0]=="r" else
            #         FadeTransform(source[int(i[1:])],target[j])
            #         for i,j in zip(*transform_index)
            #     ],
            #     run_time=3
            # )
        
        # close subtitle
        #if m_option == 3 : 
        f.close()
