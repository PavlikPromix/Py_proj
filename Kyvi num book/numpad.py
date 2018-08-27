from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
l = []


class appl(App):
    def build(self):


        gl = GridLayout(cols = 3, padding = [15], spacing = 10)

        gl.add_widget(Button(text = '7', on_press = self.com7, background_color = [.16,.17,.20, 1], background_normal = '', font_size = 22))
        gl.add_widget(Button(text = '8', on_press = self.com8, background_color = [.16,.17,.20, 1], background_normal = '', font_size = 22))
        gl.add_widget(Button(text = '9', on_press = self.com9, background_color = [.16,.17,.20, 1], background_normal = '', font_size = 22))

        gl.add_widget(Button(text = '4', on_press = self.com4, background_color = [.16,.17,.20, 1], background_normal = '', font_size = 22))
        gl.add_widget(Button(text = '5', on_press = self.com5, background_color = [.16,.17,.20, 1], background_normal = '', font_size = 22))
        gl.add_widget(Button(text = '6', on_press = self.com6, background_color = [.16,.17,.20, 1], background_normal = '', font_size = 22))

        gl.add_widget(Button(text = '1', on_press = self.com1, background_color = [.16,.17,.20, 1], background_normal = '', font_size = 22))
        gl.add_widget(Button(text = '2', on_press = self.com2, background_color = [.16,.17,.20, 1], background_normal = '', font_size = 22))
        gl.add_widget(Button(text = '3', on_press = self.com3, background_color = [.16,.17,.20, 1], background_normal = '', font_size = 22))

        gl.add_widget(Button(text = 'show & check', on_press = self.comp, background_color = [.13,.15,.17,1], background_normal = '', font_size = 22))
        gl.add_widget(Button(text = '0', on_press = self.com0, background_color = [.16,.17,.20, 1], background_normal = '', font_size = 22))
        gl.add_widget(Button(text = 'save', on_press = self.coms, background_color = [.13,.15,.17, 1], background_normal = '', font_size = 22))


        return gl
    def com0 (self, instance):
        print('0')
        if len(l)-1 <= 10:
            l.append('0')
    def com1 (self, instance):
        print('1')
        if len(l)-1 <= 10:
            l.append('1')
    def com2 (self, instance):
        print('2')
        if len(l)-1 <= 10:
            l.append('2')
    def com3 (self, instance):
        print('3')
        if len(l)-1 <= 10:
            l.append('3')
    def com4 (self, instance):
        print('4')
        if len(l)-1 <= 10:
            l.append('4')
    def com5 (self, instance):
        print('5')
        if len(l)-1 <= 10:
            l.append('5')
    def com6 (self, instance):
        print('6')
        if len(l)-1 <= 10:
            l.append('6')
    def com7 (self, instance):
        print('7')
        if len(l)-1 <= 10:
            l.append('7')
    def com8 (self, instance):
        print('8')
        if len(l)-1 <= 10:
            l.append('8')
    def com9 (self, instance):
        print('9')
        if len(l)-1 <= 10:
            l.append('9')
    def comp (self, instance):
        if len(l) == 11:
            print ('Number are full')
            print ('Number is {}{}{}{}{}{}{}{}{}{}{}'.format(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10]))
        else:
            print ('You need enter ' + str(11 - len(l)) + ' nums')
    def coms (self, instance):
        if len(l) == 11:
            fl = open ('Num.txt', 'a')
            fl.write('Number: ')
            for ka in l:
                fl.write(str(ka))
            fl.write('\n')
            fl.close()

if __name__ == '__main__':
    appl().run()
