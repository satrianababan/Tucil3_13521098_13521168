import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os
import networkx as nx
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import Utility
from Path import *
import Coordinate
import Graph
import Node
import Parser

window = tk.Tk()
window.title("Find Route")

imageframe = tk.LabelFrame(window,text="Map")
imageframe.grid(column=2,row=1,rowspan=10,columnspan=2)
Labelimage = tk.Label(imageframe,width=100,height=30)
Labelimage.pack()

labelinput = tk.Label(window,text="Input File")
labelinput.grid(column=0,row=2)
toSearch = tk.Button(window,text="Select",command=lambda:search())
toSearch.grid(column=0,row=3)
input_check = tk.Label(window,text="Belum ada file terpilih")
input_check.grid(column=0,row=4)

chooseMethod = tk.Label(window,text="Pilih Algoritma")
chooseMethod.grid(column=0,row=10)

choosePoint = tk.Label(window,text="Pilih titik")
choosePoint.grid(column=0,row=6)

ucs = tk.Button(window,text="UCS",command=lambda:ucs_search())
ucs.grid(column=0,row=11)
astar = tk.Button(window,text="A*",command=lambda:astar_search())
astar.grid(column=0,row=12)

filedirect = ''
matrix = ["empty"]
matrixGobal = []
globalCoor = []

def search():
    global filedirect
    ftypes = [('Text','*.txt')]
    filedirect = filedialog.askopenfilename(filetypes=ftypes)
    head, tail = os.path.split(filedirect)
    if(filedirect==''):
        input_check.config(text='Belum ada file')
    else:
        input_check.config(text=tail)
        nama,matriks,koor = astar.read_file(filedirect)
        if(Path.aStar.checkMatrix(matriks)):
            graf = Path.aStar.visualize_graph(nama,matriks,koor)
            global matrixGobal
            global matrix
            global globalCoor
            matrix = nama
            matrixGobal = matriks
            globalCoor = koor
            #-------visualisasi-----------
            f = plt.figure(figsize=(6.5, 4.45), dpi=100)
            ax = f.add_subplot(111)
            Path.aStar.draw_graph_koor(graf)
            canvas = FigureCanvasTkAgg(f, master=window)
            canvas.draw()
            canvas.get_tk_widget().grid(row=1, column=2,rowspan=10)
            #----------------------------------------------
            global start,end,click2,click
            start.destroy()
            start = tk.OptionMenu(window,click,*nama)
            start.grid(column=0,row=7)
            end.destroy()
            end = tk.OptionMenu(window,click2,*nama)
            end.grid(column=0,row=8)
        else:
            result.config(text="Input masih salah")

def astar_search():
    if(filedirect!=''):
        if(matrix[0]!="empty" and matrixGobal!=[] and globalCoor!=[]):
            graph = Path.aStar.matrixToGraph(matrixGobal)
            hasil = astar.astar(graph,astar.getIDXName(matrix,click.get()),astar.getIDXName(matrix,click2.get()),globalCoor)
            if(hasil!=None):
                rute = astar.printRute(hasil,matrix)
                jrk = astar.jarak(graph,hasil)
                result.config(text=rute)
                distance.config(text=jrk)
                graphvis = astar.visualgrafkoor(matrix,matrixGobal,globalCoor)
                f = plt.figure(figsize=(6.5, 4.45), dpi=100)
                ax = f.add_subplot(111)
                astar.draw_graph_koor_color(graphvis,hasil,matrix)
                canvas = FigureCanvasTkAgg(f, master=window)
                canvas.draw()
                canvas.get_tk_widget().grid(row=1, column=2,rowspan=10)
            else:
                result.config(text="Tidak menemukan rute")
                distance.config(text="")


def ucs_search():
    if(filedirect!=''):
        graph = Path.uniformCostSearch.read_graph(filedirect)
        a = click.get()
        b = click2.get()
        if(len(Path.uniformCostSearch.ucs()) > 2):
            hasil = "No path found"
        else:
            hasil, jarak = Path.uniformCostSearch.ucs()
        if(hasil=="No path found"):
            result.config(text="Tidak menemukan rute")
            distance.config(text="")
        else:
            distance.config(text=jarak)
            ha = []
            rute = "Rute : "
            for j in range(len(hasil)):
                if(j==len(hasil)-1):
                    rute+=hasil[j]
                else:
                    rute+=hasil[j]+"->"
            result.config(text=rute)
            for i in range(len(hasil)):
                ha.append(astar.getIDXName(matrix,hasil[i]))
            graphvis = astar.visualgrafkoor(matrix,matrixGobal,globalCoor)
            f = plt.figure(figsize=(6.5, 4.45), dpi=100)
            ax = f.add_subplot(111)
            astar.draw_graph_koor_color(graphvis,ha,matrix)
            canvas = FigureCanvasTkAgg(f, master=window)
            canvas.draw()
            canvas.get_tk_widget().grid(row=1, column=2,rowspan=10)
    
click = tk.StringVar()
click.set("Pilih Titik Awal")
start = tk.OptionMenu(window,click,*matrix)
start.grid(column=0,row=7)

click2 = tk.StringVar()
click2.set("Pilih Titik Akhir")
end = tk.OptionMenu(window,click2,*matrix)
end.grid(column=0,row=8)

Result = tk.Label(window,text="Result:")
Result.grid(column=0,row=13)
result = tk.Label(window,text="")
result.grid(column=1,row=13,columnspan=2)

jarak = tk.Label(window,text="Jarak:")
jarak.grid(column=0,row=15)
distance = tk.Label(window,text="")
distance.grid(column=1,row=15,columnspan=2)

judul = tk.Label(window,text="Selamat datang di pensearchan rute")
judul.grid(column=0,row=0)

window.mainloop()