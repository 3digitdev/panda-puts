import pandas as pd
import matplotlib.pyplot as plt


def show_graph():
    download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv"
    df = pd.read_csv(download_url)
    pd.set_option("display.max.columns", None)
    # Apply a style
    # Styles can be found with `print(plt.style.available)`
    # https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html
    with plt.style.context("fivethirtyeight"):
        plt.plot(df["Rank"], df["P75th"])
        # Add text at a point on the map
        #   - xy is the coordinates of the point
        #   - xytext is the offset of the text from the point
        #   - textcoords="offset pixels" is required
        plt.annotate(
            xy=[100, 100000], xytext=[8, 0], textcoords="offset pixels", text="Test"
        )
        # Add a specific point onto the map
        plt.plot([100], 100000, "ro")
        # Add a point with a label
        plt.plot([50], 100000, "ro", label="foobar")
        # Display the legend for all .plot() calls with labels
        plt.legend()
    plt.show()
