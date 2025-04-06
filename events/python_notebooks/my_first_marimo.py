import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md("""Jupyter is a great notebook environment, but there are alternatives these days.  One of them is called marimo and the whole point of the environment is that everything reactive. This means that you can write code and see changes immediately without manually running cells.""")
    return


@app.cell
def __():
    #  The first cell has
    a = 1
    return (a,)


@app.cell
def __():
    # The second cell has
    b = 11
    return (b,)


@app.cell
def __(a, b):
    # The third cell is with a + b will immediately show the sum above. But in Jupyter you would have to manually rerun the cells to see the updated result.

    # Change a or b in above two cells and observe

    a + b
    return


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    mo.md(r"""Marimo notebooks are reactive: they automatically react to your code changes and UI interactions and keep your notebook up-to-date, not unlike a spreadsheet. """)
    return


@app.cell
def __(mo):
    # When you run this cell you will now see a slider appear. However, that also means that val is now pointing to a slider object. 


    val = mo.ui.slider(1, 10, 0.1)
    val

    return (val,)


@app.cell
def __(val):
    # If you want to see the value of the slider you can do so by running the following cell.

    val.value - 2
    return


@app.cell
def __(mo):
    mo.md(r"""Add more code below!!! """)
    return


if __name__ == "__main__":
    app.run()
