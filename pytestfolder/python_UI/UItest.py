import tkinter as tk
print("Tk is ready!")

# win=tk.Tk()
# win.title("hs data analyze sys")
# win.geometry("500x500")
# apple=tk.Label(win,text="hello the world")
# apple.pack()
# win.mainloop()


class win(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("hello the world")
        self.geometry("500x500")
        function_analyzer=tk.Button(self,text="分析資料",)
        function_analyzer.grid()
        function_setting=tk.Button(self,text="設定")
        function_alam=tk.Button(self,text="警告")
        function_number=tk.Button(self,text="編號")

# if __name__=="__main__":
window=win()
window.mainloop()
