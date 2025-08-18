import streamlit as st
import pandas as pd 
import plotly.express as px
import math

st.set_page_config(layout="wide")

# CSS
st.markdown(
    """
        <style>
            label[data-testid="stWidgetLabel"] > div {
                font-size: 23px;
                color: white;
            }
            div.stHorizontalBlock:has(>div>div>div>div>div>p>span#tombol-kiri-pilih-filter) {
                display: flex;
                gap: 7px;
                div.stButton > button {
                    width: 100%;
                    height: 40px;
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 8px;    
                    padding: 10px;
                    div {
                        font-size: 20px;
                        font-weight: bold;
                    }
                }
                div.stButton > button:hover {
                    background-color: #398439;;
                    color: white;
                    font-weight: bold;
                }
                >div:nth-child(1) {
                    min-width: 40px;
                    max-width: 40px;
                }
                >div:nth-child(2) {
                    width: 100%;
                }
                >div:nth-child(3) {
                    min-width: 40px;
                    max-width: 40px;
                }
            }
            div.stHorizontalBlock:has(>div>div>div>div>div>p>span#tombol-kiri-pilih-variabel) {
                display: flex;
                gap: 7px;
                margin-bottom: -10px;
                div.stButton > button {
                    width: 100%;
                    height: 40px;
                    background-color: #FF4B4B;
                    color: white;
                    border-radius: 8px;    
                    padding: 10px;
                    div {
                        font-size: 20px;
                        font-weight: bold;
                    }
                }
                div.stButton > button:hover {
                    background-color: #CC3A3A;
                    color: white;
                    font-weight: bold;
                }
                >div:nth-child(1) {
                    min-width: 40px;
                    max-width: 40px;
                }
                >div:nth-child(2) {
                    width: 100%;
                }
                >div:nth-child(3) {
                    min-width: 40px;
                    max-width: 40px;
                }
            }
            div.stHorizontalBlock:has(>div>div>div>div>div>p>span#left-panel) {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                >div:first-child {
                    min-width: 710px;
                    max-width: 710px;
                    padding: 10px 20px 30px 20px;
                    background-color: darkgreen;
                    border-radius: 15px;
                }
                >div:nth-child(2) {
                    min-width: 600px;
                    padding: 10px 20px 40px 20px;
                    background-color: salmon;
                    border-radius: 15px;
                }
            }
            div.stHorizontalBlock:has(>div>div>div>div>div>p>span#gambar) {
                display: flex;
                >div:nth-child(1) {
                    width: 100%;
                }
                >div:nth-child(2) {
                    min-width: 245px;
                    max-width: 245px;
                    margin-top: -62px;
                }
            }
            div[data-baseweb="slider"] {
                margin-left: 10px;
                margin-top: 10px;
                margin-bottom: -10px;
                width: 650px;
            }
            div[data-baseweb="slider"] > div > div > div > div {
                color: white;
                font-size: 18px;
            }
            div[data-testid="stSliderTickBarMax"], div[data-testid="stSliderTickBarMin"] {
                display: none;
            }
            div.stButton > button {
                width: 100%;
                # margin-top:5px;
                margin-bottom:-10px;
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;    
                padding: 10px 20px;
                div {
                    font-size: 20px;
                    font-weight: bold;
                }
            }
            div.stButton > button:hover {
                background-color: #398439;
                color: white;
                font-weight: bold;
            }
        </style>
    """,
    unsafe_allow_html=True
)
title = \
    """
    <h1 style='
        margin-top: -40px;
        margin-bottom: 20px;
        text-align: center; 
        color: white; 
        background-color: navy; 
        padding: 10px; 
        border-radius: 15px;
        font-size: 42px;
        min-height: 75px;
    '>
        Customer Behavior and Shopping Habits
    </h1>
    """
dataset = \
    """
    <div style='
        margin-bottom: 5px;
        font-size: 29px;
        font-weight: bold;
        color: white;
    '>
        Dataset
    </div>
    """
subset = \
    """
    <div style='
        margin-bottom: 5px;
        font-size: 29px;
        font-weight: bold;
        color: yellow;
    '>
        Subset
    </div>
    """
pilih_filter = \
    """
    <div style='
        margin-bottom: 6px;
        font-size: 23px;
        color: white;
        text-align: center;
    '>
        Pilih Filter:
    </div>
    """
pilih_variabel = \
    """
    <div style='
        margin-bottom: 6px;
        font-size: 23px;
        color: white;
        text-align: center;
    '>
        Pilih Variabel:
    </div>
    """

# KODE
df = pd.read_csv("shopping_trends.csv")

st.markdown(title, unsafe_allow_html=True)

left, right = st.columns(2)
with left:
    st.markdown(pilih_filter, unsafe_allow_html=True)
    list_pilihan = df.columns.to_list()[1:]
    if "filter" not in st.session_state:
        st.session_state["filter"] = list_pilihan[0]
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        def prev_filter():
            current_index = list_pilihan.index(st.session_state["filter"])
            st.session_state["filter"] = list_pilihan[(current_index - 1) % len(list_pilihan)]
        st.button("⮜", key="prev_filter_button", on_click=prev_filter)
        st.markdown("<span id='tombol-kiri-pilih-filter' style='display:none;'></span>", unsafe_allow_html=True)
    with col2:
        filter = st.selectbox(
            "",
            list_pilihan,
            label_visibility="collapsed",
            key="filter"
        )
    with col3:
        def next_filter():
            current_index = list_pilihan.index(st.session_state["filter"])
            st.session_state["filter"] = list_pilihan[(current_index + 1) % len(list_pilihan)]
        st.button("⮞", key="next_filter_button", on_click=next_filter)

    min_usia, max_usia = int(df['Age'].min()), int(df['Age'].max())       
    if "range_slider" not in st.session_state:
        st.session_state["range_slider"] = (min_usia, max_usia)
    range_usia = st.slider(
        "Filter Usia:",
        min_usia, max_usia,
        key="range_slider"
    )

    default_gender = "Semua Gender"
    genders = [default_gender, "Male", "Female"]
    if "gender" not in st.session_state:
        st.session_state["gender"] = default_gender
    filter_gender = st.selectbox(
        "Filter Gender:",
        options=genders,
        key="gender"
    )

    locations = df['Location'].dropna().unique().tolist()
    default_location = "Semua Lokasi"
    locations.sort()
    locations.insert(0, default_location)
    if "location" not in st.session_state:
        st.session_state["location"] = default_location
    filter_location = st.selectbox(
        "Filter Lokasi:",
        options=locations,
        key="location"
    )

    default_season = "Semua Musim"
    seasons = [default_season, "Spring", "Summer", "Fall", "Winter"]
    if "season" not in st.session_state:
        st.session_state["season"] = default_season
    filter_season = st.selectbox(
        "Filter Musim:",
        options=seasons,
        key="season"
    )

    df_filter = df[
        (df['Age'].between(range_usia[0], range_usia[1])) &
        ((filter_gender == default_gender) or (df['Gender'] == filter_gender)) &
        ((filter_location == default_location) or (df['Location'] == filter_location)) &
        ((filter_season == default_season) or (df['Season'] == filter_season))
    ]

    def reset_session():
        st.session_state["range_slider"] = (min_usia, max_usia)
        st.session_state["genders"] = default_gender
        st.session_state["location"] = default_location
        st.session_state["season"] = default_season
    st.button("Reset Filter", on_click=reset_session)

    if len(df_filter) != len(df):
        st.markdown(subset, unsafe_allow_html=True)
        warna = "yellow"
    else:
        st.markdown(dataset, unsafe_allow_html=True)
        warna = "white"
    st.dataframe(df_filter, height=391)
    st.markdown(f"<div style='margin-top:-20px; padding: 0px 5px; color:white; font-size:20px; text-align:right;'> \
        <span style='color:{warna}; font-weight:bold;'>{len(df_filter)}</span> Transaksi</div>", unsafe_allow_html=True)
    st.markdown("<span id='left-panel' style='display:none;'></span>", unsafe_allow_html=True)

with right:
    st.markdown(pilih_variabel, unsafe_allow_html=True)
    list_pilihan = df.columns.to_list()[1:]
    if "variabel" not in st.session_state:
        st.session_state["variabel"] = list_pilihan[0]
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        def prev_variabel():
            current_index = list_pilihan.index(st.session_state["variabel"])
            st.session_state["variabel"] = list_pilihan[(current_index - 1) % len(list_pilihan)]
        st.button("⮜", key="prev_variabel_button", on_click=prev_variabel)
        st.markdown("<span id='tombol-kiri-pilih-variabel' style='display:none;'></span>", unsafe_allow_html=True)
    with col2:
        pilihan = st.selectbox(
            "",
            list_pilihan,
            label_visibility="collapsed",
            key="variabel"
        )
    with col3:
        def next_variabel():
            current_index = list_pilihan.index(st.session_state["variabel"])
            st.session_state["variabel"] = list_pilihan[(current_index + 1) % len(list_pilihan)]
        st.button("⮞", key="next_variabel_button", on_click=next_variabel)

    if pilihan == "Age":
        min_age = df_filter["Age"].min()
        max_age = df_filter["Age"].max() + 1
        size_age = (max_age - min_age)//10
        if (max_age - min_age)%10 > 0:
            size_age = size_age + 1
        fig = px.histogram(df_filter, x="Age", labels={"Age": "Usia", "count": "Jumlah Pelanggan"}, height=600, title="Distribusi Usia Pelanggan") 
        fig.update_traces(
            xbins=dict(
                start=min_age,
                end=max_age,
                size=size_age
            ),
            texttemplate="<b>%{y}</b>",
            hovertemplate="Usia: <b>%{x}</b><br>Jumlah Pelanggan: <b>%{y}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color="#5799c6", 
            marker_line_color="black",
            marker_line_width=1,
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Usia",
            yaxis_title="Jumlah Pelanggan",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ],
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14), range=[min_age-5, max_age+5])
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Gender":
        gender_counts = df_filter["Gender"].value_counts().reset_index()
        gender_counts.columns = ["Gender", "Jumlah Pelanggan"]
        gender_dict_colors = {
            "Male": "#3274A1",
            "Female": "#E1812C"
        }
        gender_colors = list(map(lambda x:gender_dict_colors[x], gender_counts["Gender"].to_list()))

        # Bar chart
        fig = px.bar(
            gender_counts,
            x="Gender",
            y="Jumlah Pelanggan",
            height=600,
            title="Distribusi Gender Pelanggan"
        )
        fig.update_traces(
            texttemplate="<b>%{y}</b>",
            hovertemplate="Gender: <b>%{x}</b><br>Jumlah Pelanggan: <b>%{y}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=gender_colors
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Gender",
            yaxis_title="Jumlah Pelanggan",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ]
        )
        try:
            y_max = max([max(trace.y) for trace in fig.data if hasattr(trace, "y")])
        except:
            y_max = 0
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14), range=[0, y_max*1.15])
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

        # Pie chart
        fig = px.pie(
            gender_counts,
            names="Gender",
            values="Jumlah Pelanggan",
            height=600,
            title="Proporsi Gender Pelanggan",
        )
        fig.update_traces(
            textinfo="percent+label",
            hovertemplate="Gender: <b>%{label}</b><br>Persen: <b>%{percent}</b><extra></extra>",
            hoverlabel=dict(font_color="black", font_size=18),
            insidetextfont=dict(color="white", size=16),
            marker=dict(colors=gender_colors)
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Item Purchased":
        top_10_items = df_filter["Item Purchased"].value_counts().head(10)[::-1]
        df_top10 = top_10_items.reset_index()
        df_top10.columns = ["Produk", "Frekuensi Pembelian"]
        fig = px.bar(
            df_top10,
            x="Frekuensi Pembelian",
            y="Produk",
            orientation="h",
            text="Frekuensi Pembelian",
            height=600,
            title="Distribusi Produk Dengan Pembelian Terbanyak",
        )
        fig.update_traces(
            texttemplate="<b>%{x}</b>",
            hovertemplate="Produk: <b>%{y}</b><br>Frekuensi Pembelian: <b>%{x}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=["#2EABB8", "#845B53", "#C03D3E", "#7F7F7F", "#E1812C", "#9372B2", "#3A923A", "#A9AA35", "#D684BD", "#3274A1"],
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Frekuensi Pembelian",
            yaxis_title="Produk",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ],
            showlegend=False,
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Category":
        top_categories = df_filter["Category"].value_counts()[::-1]
        df_categories = top_categories.reset_index()
        df_categories.columns = ["Kategori Produk", "Frekuensi Pembelian"]
        fig = px.bar(
            df_categories,
            x="Frekuensi Pembelian",
            y="Kategori Produk",
            orientation="h",
            text="Frekuensi Pembelian",
            height=600,
            title="Distribusi Kategori Produk Dengan Pembelian Terbanyak",
        )
        fig.update_traces(
            texttemplate="<b>%{x}</b>",
            hovertemplate="Kategori Produk: <b>%{y}</b><br>Frekuensi Pembelian: <b>%{x}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=["#3a932a", "#E1812C", "#C03D3E", "#3274A1"],
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Frekuensi Pembelian",
            yaxis_title="Kategori Produk",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ],
            showlegend=False,
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Purchase Amount (USD)":
        min_amount = df_filter["Purchase Amount (USD)"].min()
        max_amount = df_filter["Purchase Amount (USD)"].max() + 1
        size_amount = (max_amount - min_amount)//10
        if (max_amount - min_amount)%10 > 0:
            size_amount =size_amount + 1
        fig = px.histogram(df_filter, x="Purchase Amount (USD)", height=600, title="Distribusi Nilai Pembelian") 
        fig.update_traces(
            xbins=dict(
                start=min_amount,
                end=max_amount,
                size=size_amount
            ),
            texttemplate="<b>%{y}</b>",
            hovertemplate="Nilai Pembelian: <b>%{x}</b> USD<br>Frekuensi Transaksi: <b>%{y}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color="#5799c6", 
            marker_line_color="black",
            marker_line_width=1,
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Nilai Pembelian (USD)",
            yaxis_title="Frekuensi Transaksi",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ]
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14), range=[min_amount-5, max_amount+5])
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Location":
        top_locations = df_filter["Location"].value_counts().head(10)[::-1]
        df_locations = top_locations.reset_index()
        df_locations.columns = ["Lokasi", "Frekuensi Pembelian"]
        fig = px.bar(
            df_locations,
            x="Frekuensi Pembelian",
            y="Lokasi",
            orientation="h",
            text="Frekuensi Pembelian",
            height=600,
            title="Distribusi Lokasi Dengan Pembelian Terbanyak",
        )
        fig.update_traces(
            texttemplate="<b>%{x}</b>",
            hovertemplate="Lokasi: <b>%{y}</b><br>Frekuensi Pembelian: <b>%{x}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=["#E1812C", "#A9AA35", "#845B53", "#3A923A", "#2EABB8", "#C03D3E", "#D684BD", "#7F7F7F", "#9372B2", "#3274A1"],
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Frekuensi Pembelian",
            yaxis_title="Lokasi",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ],
            showlegend=False,
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Size":
        size_order = ["S", "M", "L", "XL"]
        size_counts = df_filter["Size"].value_counts().reindex(size_order).reset_index()
        size_counts.columns = ["Ukuran Produk", "Frekuensi Pembelian"]
        fig = px.bar(
            size_counts,
            x="Ukuran Produk",
            y="Frekuensi Pembelian",
            height=600,
            title="Distribusi Ukuran Produk"
        )
        fig.update_traces(
            texttemplate="<b>%{y}</b>",
            hovertemplate="Ukuran Produk: <b>%{x}</b><br>Frekuensi Pembelian: <b>%{y}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=["#E1812C","#3A923A", "#3274A1", "#C03D3E"]
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Ukuran Produk",
            yaxis_title="Frekuensi Pembelian",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ]
        )
        y_max = max([max(trace.y) for trace in fig.data if hasattr(trace, "y")])
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14), range=[0, y_max*1.15])
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Color":
        top_10_colors = df_filter["Color"].value_counts().head(10)[::-1]
        list_color = top_10_colors.index.to_list() 
        df_top10 = top_10_colors.reset_index()
        df_top10.columns = ["Warna Produk", "Frekuensi Pembelian"]
        fig = px.bar(
            df_top10,
            x="Frekuensi Pembelian",
            y="Warna Produk",
            orientation="h",
            text="Frekuensi Pembelian",
            height=600,
            title="Distribusi Warna Produk Dengan Pembelian Terbanyak",
        )
        fig.update_traces(
            texttemplate="<b>%{x}</b>",
            hovertemplate="Warna Produk: <b>%{y}</b><br>Frekuensi Pembelian: <b>%{x}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=list_color,
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Frekuensi Pembelian",
            yaxis_title="Warna Produk",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ],
            showlegend=False,
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Season":
        season_order = ["Spring", "Summer", "Fall", "Winter"]
        season_counts = df_filter["Season"].value_counts().reindex(season_order).reset_index().dropna()
        season_counts.columns = ["Musim", "Frekuensi Pembelian"]
        season_dict_colors = {
            "Spring": "#E1812C",
            "Summer": "#3A923A",
            "Fall": "#C03D3E",
            "Winter": "#3274A1"
        }
        season_colors = list(map(lambda x:season_dict_colors[x], season_counts["Musim"].to_list()))
        fig = px.bar(
            season_counts,
            x="Musim",
            y="Frekuensi Pembelian",
            height=600,
            title="Distribusi Musim"
        )
        fig.update_traces(
            texttemplate="<b>%{y}</b>",
            hovertemplate="Musim: <b>%{x}</b><br>Frekuensi Pembelian: <b>%{y}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=season_colors
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Musim",
            yaxis_title="Frekuensi Pembelian",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ]
        )
        y_max = max([max(trace.y) for trace in fig.data if hasattr(trace, "y")])
        fig.update_yaxes(range=[0, y_max*1.15])
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Review Rating":
        try:
            min_rating = math.floor(df_filter["Review Rating"].min())
            max_rating = math.ceil(df_filter["Review Rating"].max()) + 0.1
        except:
            min_rating = 0
            max_rating = 0
        fig = px.histogram(df_filter, x="Review Rating", nbins=12, labels={"Review Rating": "Rating", "count": "Jumlah Produk"}, height=600, title="Distribusi Rating Produk") 
        fig.update_traces(
            # xbins=dict(
            #     start=min_rating,
            #     end=max_rating,
            #     size=0.5
            # ),
            texttemplate="<b>%{y}</b>",
            hovertemplate="Rating: <b>%{x}</b><br>Jumlah Produk: <b>%{y}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color="#5799c6", 
            marker_line_color="black",
            marker_line_width=1,
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Rating",
            yaxis_title="Jumlah Produk",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ],
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14), range=[min_rating, max_rating])
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)


    if pilihan == "Subscription Status":
        status_order = ["Yes", "No"]
        status_counts = df_filter["Subscription Status"].value_counts().reindex(status_order).reset_index()
        status_counts.columns = ["Status Berlangganan", "Jumlah Pelanggan"]
        # Bar chart
        fig = px.bar(
            status_counts,
            x="Status Berlangganan",
            y="Jumlah Pelanggan",
            height=600,
            title="Distribusi Status Berlangganan"
        )
        fig.update_traces(
            texttemplate="<b>%{y}</b>",
            hovertemplate="Status Berlangganan: <b>%{x}</b><br>Jumlah Pelanggan: <b>%{y}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=["#3274A1","#E1812C"]
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Status Berlangganan",
            yaxis_title="Jumlah Pelanggan",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ]
        )
        y_max = max([max(trace.y) for trace in fig.data if hasattr(trace, "y")])
        fig.update_yaxes(range=[0, y_max*1.15])
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

        # Pie chart
        fig = px.pie(
            status_counts,
            names="Status Berlangganan",
            values="Jumlah Pelanggan",
            height=600,
            title="Proporsi Status Berlangganan",
        )
        fig.update_traces(
            textinfo="percent+label",
            hovertemplate="Status Berlangganan: <b>%{label}</b><br>Persen: <b>%{percent}</b><extra></extra>",
            hoverlabel=dict(font_color="black", font_size=18),
            insidetextfont=dict(color="white", size=16),
            marker=dict(colors=["#3274A1", "#E1812C"]),
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Payment Method":
        top_methods = df_filter["Payment Method"].value_counts()[::-1]
        df_methods = top_methods.reset_index()
        df_methods.columns = ["Metode Pembayaran", "Jumlah Transaksi"]
        fig = px.bar(
            df_methods,
            x="Jumlah Transaksi",
            y="Metode Pembayaran",
            orientation="h",
            text="Jumlah Transaksi",
            height=600,
            title="Distribusi Metode Pembayaran",
        )
        fig.update_traces(
            texttemplate="<b>%{x}</b>",
            hovertemplate="Metode Pembayaran: <b>%{y}</b><br>Jumlah Transaksi: <b>%{x}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=["#E1812C", "#845B53", "#C03D3E", "#3A923A", "#9372B2", "#3274A1"],
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Jumlah Transaksi",
            yaxis_title="Metode Pemabayaran",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ],
            showlegend=False,
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Shipping Type":
        top_shippings = df_filter["Shipping Type"].value_counts()[::-1]
        df_shippings = top_shippings.reset_index()
        df_shippings.columns = ["Jenis Pengiriman", "Jumlah Transaksi"]
        fig = px.bar(
            df_shippings,
            x="Jumlah Transaksi",
            y="Jenis Pengiriman",
            orientation="h",
            text="Jumlah Transaksi",
            height=600,
            title="Distribusi Jenis Pengiriman Produk",
        )
        fig.update_traces(
            texttemplate="<b>%{x}</b>",
            hovertemplate="Jenis Pengiriman: <b>%{y}</b><br>Jumlah Transaksi: <b>%{x}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=["#9372B2", "#3274A1", "#3A923A", "#845B53", "#C03D3E", "#E1812C"],
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Jumlah Transaksi",
            yaxis_title="Jenis Pengiriman",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ],
            showlegend=False,
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Discount Applied":
        discounts_order = ["Yes", "No"]
        discounts_counts = df_filter["Discount Applied"].value_counts().reindex(discounts_order).reset_index()
        discounts_counts.columns = ["Diskon Diterapkan", "Frekuensi Pembelian"]
        # Bar chart
        fig = px.bar(
            discounts_counts,
            x="Diskon Diterapkan",
            y="Frekuensi Pembelian",
            height=600,
            title="Distribusi Diskon Diterapkan Pada Pembelian"
        )
        fig.update_traces(
            texttemplate="<b>%{y}</b>",
            hovertemplate="Diskon Diterapkan: <b>%{x}</b><br>Frekuensi Pembelian: <b>%{y}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=["#3274A1","#E1812C"]
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Diskon Diterapkan",
            yaxis_title="Frekuensi Pembelian",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ]
        )
        y_max = max([max(trace.y) for trace in fig.data if hasattr(trace, "y")])
        fig.update_yaxes(range=[0, y_max*1.15])
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

        # Pie chart
        fig = px.pie(
            discounts_counts,
            names="Diskon Diterapkan",
            values="Frekuensi Pembelian",
            height=600,
            title="Proporsi Diskon Diterapkan Pada Pembelian",
        )
        fig.update_traces(
            textinfo="percent+label",
            hovertemplate="Diskon Diterapkan: <b>%{label}</b><br>Persen: <b>%{percent}</b><extra></extra>",
            hoverlabel=dict(font_color="black", font_size=18),
            insidetextfont=dict(color="white", size=16),
            marker=dict(colors=["#3274A1", "#E1812C"]),
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Promo Code Used":
        promo_order = ["Yes", "No"]
        promo_counts = df_filter["Promo Code Used"].value_counts().reindex(promo_order).reset_index()
        promo_counts.columns = ["Kode Promosi Digunakan", "Frekuensi Pembelian"]
        # Bar chart
        fig = px.bar(
            promo_counts,
            x="Kode Promosi Digunakan",
            y="Frekuensi Pembelian",
            height=600,
            title="Distribusi Kode Promosi Digunakan Pada Pembelian"
        )
        fig.update_traces(
            texttemplate="<b>%{y}</b>",
            hovertemplate="Kode Promosi Digunakan: <b>%{x}</b><br>Frekuensi Pembelian: <b>%{y}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=["#3274A1","#E1812C"]
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Kode Promosi Digunakan",
            yaxis_title="Frekuensi Pembelian",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ]
        )
        y_max = max([max(trace.y) for trace in fig.data if hasattr(trace, "y")])
        fig.update_yaxes(range=[0, y_max*1.15])
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

        # Pie chart
        fig = px.pie(
            promo_counts,
            names="Kode Promosi Digunakan",
            values="Frekuensi Pembelian",
            height=600,
            title="Proporsi Kode Promosi Digunakan Pada Pembelian",
        )
        fig.update_traces(
            textinfo="percent+label",
            hovertemplate="Kode Promosi Digunakan: <b>%{label}</b><br>Persen: <b>%{percent}</b><extra></extra>",
            hoverlabel=dict(font_color="black", font_size=18),
            insidetextfont=dict(color="white", size=16),
            marker=dict(colors=["#3274A1", "#E1812C"]),
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Previous Purchases":
        min_purchase = df_filter["Previous Purchases"].min()
        max_purchase = df_filter["Previous Purchases"].max() + 1
        size_purchase = (max_purchase - min_purchase)//10
        if (max_purchase - min_purchase)%10 > 0:
            size_purchase = size_purchase + 1
        fig = px.histogram(df_filter, x="Previous Purchases", labels={"Previous Purchases": "Jumlah Pembelian Sebelumnya",
            "count": "Jumlah Pelanggan"}, height=600, title="Distribusi Jumlah Pembelian Pelanggan Sebelumnya") 
        fig.update_traces(
            xbins=dict(
                start=min_purchase,
                end=max_purchase,
                size=size_purchase
            ),
            texttemplate="<b>%{y}</b>",
            hovertemplate="Jumlah Pembelian Sebelumnya: <b>%{x}</b><br>Jumlah Pelanggan: <b>%{y}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color="#5799c6", 
            marker_line_color="black",
            marker_line_width=1,
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Jumlah Pembelian Sebelumnya",
            yaxis_title="Jumlah Pelanggan",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ],
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14), range=[min_purchase-5, max_purchase+5])
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Preferred Payment Method":
        top_methods = df_filter["Preferred Payment Method"].value_counts()[::-1]
        df_methods = top_methods.reset_index()
        df_methods.columns = ["Metode Pembayaran Yang Disukai", "Jumlah Pelanggan"]
        fig = px.bar(
            df_methods,
            x="Jumlah Pelanggan",
            y="Metode Pembayaran Yang Disukai",
            orientation="h",
            text="Jumlah Pelanggan",
            height=600,
            title="Distribusi Metode Pembayaran Yang Disukai Pelanggan",
        )
        fig.update_traces(
            texttemplate="<b>%{x}</b>",
            hovertemplate="Metode Pembayaran Yang Disukai: <b>%{y}</b><br>Jumlah Pelanggan: <b>%{x}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=["#9372B2", "#3274A1", "#845B53", "#E1812C", "#3A923A", "#C03D3E"],
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Jumlah Pelanggan",
            yaxis_title="Metode Pemabayaran Yang Disukai",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ],
            showlegend=False,
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Frequency of Purchases":
        top_purchases = df_filter["Frequency of Purchases"].value_counts()[::-1]
        df_purchases = top_purchases.reset_index()
        df_purchases.columns = ["Frekuensi Pembelian", "Jumlah Pelanggan"]
        fig = px.bar(
            df_purchases,
            x="Jumlah Pelanggan",
            y="Frekuensi Pembelian",
            orientation="h",
            text="Jumlah Pelanggan",
            height=600,
            title="Distribusi Frekuensi Pembelian Pelanggan",
        )
        fig.update_traces(
            texttemplate="<b>%{x}</b>",
            hovertemplate="Frekuensi Pembelian: <b>%{y}</b><br>Jumlah Pelanggan: <b>%{x}</b><extra></extra>",
            textfont=dict(color="gray", style="italic", size=12),
            hoverlabel=dict(font_color="black", font_size=18),
            textposition="outside",
            marker_color=["#E1812C", "#3274A1", "#9372B2", "#845B53", "#C03D3E", "#3A923A", "#D684BD"],
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            xaxis_title="Jumlah Pelanggan",
            yaxis_title="Frekuensi Pembelian",
            xaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            yaxis=dict(title_font=dict(size=20, color="black", weight="bold")),
            margin=dict(l=100, r=50, t=120, b=80),
            plot_bgcolor="white",
            shapes=[
                dict(
                    type="rect",
                    xref="paper", yref="paper",
                    x0=0, y0=0, x1=1, y1=1,
                    line=dict(color="black", width=1)
                )
            ],
            showlegend=False,
        )
        fig.update_xaxes(tickfont=dict(color="black", size=14))
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

st.markdown("<div style='background-color: gray; color: white; width: 100%; border-radius: 15px; padding: 20px;'> \
    <div style='width: 200px; background-color: white; color: gray; font-size: 40px; border-radius: 15px; text-align: center; font-weight: bold; padding: 0px;'>INFO</div> \
    <div style='margin-top: 10px; color: white; font-size: 23px;'> \
    <div style='margin-top: 12px; margin-bottom: 3px;'>Aplikasi EDA ini dibuat di Bandung, tanggal 17 Agustus 2025</div> \
    <div style='display:flex'><div style='width:220px;'>Nama Pembuat</div><div>: &nbsp; </div><div><span style='font-weight: bold;'>Elsa Sofiari</span></div></div> \
    <div style='display:flex'><div style='width:220px;'>Judul Proyek</div><div>: &nbsp; </div><div>Mini Project EDA (Exploratory Data Analysis)</div></div> \
    <div style='display:flex'><div style='width:220px;'>Program Bootcamp</div><div>: &nbsp; </div><div>Data Science For Beginner - Batch 13</div></div> \
    <div style='display:flex'><div style='width:220px;'>Diselenggarakan oleh</div><div>: &nbsp; </div><div>Intelligo.ID</div></div> \
    <div style='margin-top: 20px; text-align: right'><div style='display: inline-block; width:240px; height: 50px; background-color: white; border-radius: 8px;'>&nbsp;</div></div> \
    </div> \
    </div>", unsafe_allow_html=True)

footer_left, footer_right = st.columns(2)
with footer_right:
    st.image("logo-intelligo-id.png")
    st.markdown("<span id='gambar' style='display:none;'></span>", unsafe_allow_html=True)
st.markdown("<div style='display: grid; grid-template-columns: auto 260px;'><div></div> \
    <a target='_blank' href='https://www.intelligo.id/' style='margin-top: -86px; width:240px; height: 50px; background-color: transparent; border-radius: 15px;'>&nbsp;</a></div>",
    unsafe_allow_html=True)
