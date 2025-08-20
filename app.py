import streamlit as st
import pandas as pd 
import plotly.express as px
import math
import random

st.set_page_config(layout="wide")

# CSS
st.markdown(
    """
        <style>
            label[data-testid="stWidgetLabel"] > div {
                font-size: 20px;
                color: white;
                text-align: center;
            }
            div.stHorizontalBlock:has(>div>div>div>div>div>p>span#tombol-kiri-pilih-filter),
            div.stHorizontalBlock:has(>div>div>div>div>div>p>span.tombol-kiri-detail-filter) {
                display: flex;
                gap: 7px;
                div.stButton > button {
                    margin-top: 0px;
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
                    margin-top: 0px;
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
                    padding: 10px 20px 00px 20px;
                    background-color: darkgreen;
                    border-radius: 15px;
                }
                >div:nth-child(2) {
                    min-width: 600px;
                    padding: 10px 20px 20px 20px;
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
                margin-bottom: 15px;
                width: 650px;
            }
            div[data-baseweb="slider"] > div > div > div > div {
                color: white;
                font-size: 18px;
            }
            div[data-testid="stSliderTickBarMax"], div[data-testid="stSliderTickBarMin"] {
                display: none;
            }
            div.stElementContainer {
                width: 100% !important;
            }
            div.stButton > button {
                width: 100%;
                margin-top: -30px;
                margin-bottom: 0px;
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;    
                padding: 10px;
                div {
                    font-size: 20px;
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
        Pilihan Filter
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
        Pilihan Variabel
    </div>
    """

# Kode
df = pd.read_csv("shopping_trends.csv")

st.markdown(title, unsafe_allow_html=True)

left, right = st.columns(2)
with left:
    st.markdown(pilih_filter, unsafe_allow_html=True)
    default_filter_option = ""
    filter_options = df.columns.to_list()
    filter_options[0] = default_filter_option
    active_filters = {}
    for filter in filter_options[1:]:
        active_filters[filter] = "Semua"
    if "filter" not in st.session_state:
        st.session_state["filter"] = default_filter_option
    col1, col2, col3 = st.columns(3)
    with col1:
        def prev_filter():
            current_index = filter_options.index(st.session_state["filter"])
            st.session_state["filter"] = filter_options[(current_index - 1) % len(filter_options)]
        st.button("⮜", key="prev_filter_button", on_click=prev_filter)
        st.markdown("<span id='tombol-kiri-pilih-filter' style='display:none;'></span>", unsafe_allow_html=True)
    with col2:
        filter = st.selectbox(
            "",
            filter_options,
            label_visibility="collapsed",
            key="filter"
        )
    with col3:
        def next_filter():
            current_index = filter_options.index(st.session_state["filter"])
            st.session_state["filter"] = filter_options[(current_index + 1) % len(filter_options)]
        st.button("⮞", key="next_filter_button", on_click=next_filter)

    if filter == default_filter_option:
        placeholder = st.empty()
    else:
        placeholder_title = st.empty()
        placeholder = st.empty()

    min_usia, max_usia = int(df['Age'].min()), int(df['Age'].max())
    if "range_slider" not in st.session_state:
        st.session_state["range_slider"] = (min_usia, max_usia)
        st.session_state["range_slider_temp"] = (min_usia, max_usia)
    if filter == 'Age':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Rentang Usia Pelanggan:</div>", unsafe_allow_html=True)
        with placeholder.container():
            range_usia = st.slider(
                "Filter Usia:",
                min_usia, max_usia,
                value=st.session_state["range_slider"],
                label_visibility="collapsed",
            )
            st.session_state["range_slider_temp"] = range_usia
            active_filters['Age'] = f"{range_usia[0]} - {range_usia[1]}"
            if active_filters['Age'] == f"{min_usia} - {max_usia}":
                active_filters['Age'] = "Semua"
    else:
        st.session_state["range_slider"] = st.session_state["range_slider_temp"]
        range_usia = st.session_state["range_slider"]
        active_filters['Age'] = f"{range_usia[0]} - {range_usia[1]}"
        if active_filters['Age'] == f"{min_usia} - {max_usia}":
            active_filters['Age'] = "Semua"

    default_gender = "Semua"
    genders = [default_gender, "Male", "Female"]
    if "gender" not in st.session_state:
        st.session_state["gender"] = default_gender
        st.session_state["gender_temp"] = default_gender
    old_gender = st.session_state["gender"]
    if filter == 'Gender':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Gender Pelanggan:</div>", unsafe_allow_html=True)
        with placeholder.container():
            gender_col1, gender_col2, gender_col3 = st.columns(3)
            with gender_col1:
                def gender_prev_filter():
                    gender_current_index = genders.index(st.session_state["gender_temp"])
                    st.session_state["gender"] = genders[(gender_current_index - 1) % len(genders)]
                st.button("⮜", key="gender_prev_filter_button", on_click=gender_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with gender_col2:
                st.session_state['gender'] = old_gender
                st.session_state['gender_temp'] = old_gender
                filter_gender = st.selectbox(
                    'Filter Gender:',
                    options=genders,
                    label_visibility="collapsed",
                    key="gender"
                )
                st.session_state["gender_temp"] = filter_gender
                active_filters['Gender'] = filter_gender
            with gender_col3:
                def gender_next_filter():
                    gender_current_index = genders.index(st.session_state["gender_temp"])
                    st.session_state["gender"] = genders[(gender_current_index + 1) % len(genders)]
                st.button("⮞", key="gender_next_filter_button", on_click=gender_next_filter)
    else:
        st.session_state["gender"] = st.session_state["gender_temp"]
        filter_gender = st.session_state["gender"]
        active_filters['Gender'] = filter_gender

    default_item = "Semua"
    items = df['Item Purchased'].dropna().unique().tolist()
    items.sort()
    items.insert(0, default_item)
    if "item" not in st.session_state:
        st.session_state["item"] = default_item
        st.session_state["item_temp"] = default_item
    old_item = st.session_state["item"]
    if filter == 'Item Purchased':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Produk:</div>", unsafe_allow_html=True)
        with placeholder.container():
            item_col1, item_col2, item_col3 = st.columns(3)
            with item_col1:
                def item_prev_filter():
                    item_current_index = items.index(st.session_state["item_temp"])
                    st.session_state["item"] = items[(item_current_index - 1) % len(items)]
                st.button("⮜", key="item_prev_filter_button", on_click=item_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with item_col2:
                st.session_state['item'] = old_item
                st.session_state['item_temp'] = old_item
                filter_item = st.selectbox(
                    "Filter Produk:",
                    options=items,
                    label_visibility="collapsed",
                    key="item"
                )
                st.session_state["item_temp"] = filter_item
                active_filters['Item Purchased'] = filter_item
            with item_col3:
                def item_next_filter():
                    item_current_index = items.index(st.session_state["item_temp"])
                    st.session_state["item"] = items[(item_current_index + 1) % len(items)]
                st.button("⮞", key="item_next_filter_button", on_click=item_next_filter)
    else:
        st.session_state["item"] = st.session_state["item_temp"]
        filter_item = st.session_state["item"]
        active_filters['Item Purchased'] = filter_item

    default_category = "Semua"
    categories = df['Category'].dropna().unique().tolist()
    categories.sort()
    categories.insert(0, default_category)
    if "category" not in st.session_state:
        st.session_state["category"] = default_category
        st.session_state["category_temp"] = default_category
    old_category = st.session_state["category"]
    if filter == 'Category':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Kategori Produk:</div>", unsafe_allow_html=True)
        with placeholder.container():
            category_col1, category_col2, category_col3 = st.columns(3)
            with category_col1:
                def category_prev_filter():
                    category_current_index = categories.index(st.session_state["category_temp"])
                    st.session_state["category"] = categories[(category_current_index - 1) % len(categories)]
                st.button("⮜", key="category_prev_filter_button", on_click=category_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with category_col2:
                st.session_state['category'] = old_category
                st.session_state['category_temp'] = old_category
                filter_category = st.selectbox(
                    "Filter Kategori:",
                    options=categories,
                    label_visibility="collapsed",
                    key="category"
                )
                st.session_state["category_temp"] = filter_category
                active_filters['Category'] = filter_category
            with category_col3:
                def category_next_filter():
                    category_current_index = categories.index(st.session_state["category_temp"])
                    st.session_state["category"] = categories[(category_current_index + 1) % len(categories)]
                st.button("⮞", key="category_next_filter_button", on_click=category_next_filter)
    else:
        st.session_state["category"] = st.session_state["category_temp"]
        filter_category = st.session_state["category"]
        active_filters['Category'] = filter_category

    min_purchase, max_purchase = int(df['Purchase Amount (USD)'].min()), int(df['Purchase Amount (USD)'].max())
    if "range_purchase" not in st.session_state:
        st.session_state["range_purchase"] = (min_purchase, max_purchase)
        st.session_state["range_purchase_temp"] = (min_purchase, max_purchase)
    if filter == 'Purchase Amount (USD)':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Rentang Nilai Pembelian (USD):</div>", unsafe_allow_html=True)
        with placeholder.container():
            range_purchase = st.slider(
                "Filter Nilai Pembelian:",
                min_purchase, max_purchase,
                value=st.session_state["range_purchase"],
                label_visibility="collapsed",
            )
            st.session_state["range_purchase_temp"] = range_purchase
            active_filters['Purchase Amount (USD)'] = f"{range_purchase[0]} - {range_purchase[1]}"
            if active_filters['Purchase Amount (USD)'] == f"{min_purchase} - {max_purchase}":
                active_filters['Purchase Amount (USD)'] = "Semua"
    else:
        st.session_state["range_purchase"] = st.session_state["range_purchase_temp"]
        range_purchase = st.session_state["range_purchase"]
        active_filters['Purchase Amount (USD)'] = f"{range_purchase[0]} - {range_purchase[1]}"
        if active_filters['Purchase Amount (USD)'] == f"{min_purchase} - {max_purchase}":
            active_filters['Purchase Amount (USD)'] = "Semua"

    default_location = "Semua"
    locations = df['Location'].dropna().unique().tolist()
    locations.sort()
    locations.insert(0, default_location)
    if "location" not in st.session_state:
        st.session_state["location"] = default_location
        st.session_state["location_temp"] = default_location
    old_location = st.session_state["location"]
    if filter == 'Location':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Lokasi:</div>", unsafe_allow_html=True)
        with placeholder.container():
            location_col1, location_col2, location_col3 = st.columns(3)
            with location_col1:
                def location_prev_filter():
                    location_current_index = locations.index(st.session_state["location_temp"])
                    st.session_state["location"] = locations[(location_current_index - 1) % len(locations)]
                st.button("⮜", key="location_prev_filter_button", on_click=location_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with location_col2:
                st.session_state['location'] = old_location
                st.session_state['location_temp'] = old_location
                filter_location = st.selectbox(
                    "Filter Lokasi:",
                    options=locations,
                    label_visibility="collapsed",
                    key="location"
                )
                st.session_state["location_temp"] = filter_location
                active_filters['Location'] = filter_location
            with location_col3:
                def location_next_filter():
                    location_current_index = locations.index(st.session_state["location_temp"])
                    st.session_state["location"] = locations[(location_current_index + 1) % len(locations)]
                st.button("⮞", key="location_next_filter_button", on_click=location_next_filter)
    else:
        st.session_state["location"] = st.session_state["location_temp"]
        filter_location = st.session_state["location"]
        active_filters['Location'] = filter_location

    default_size = "Semua"
    sizes = [default_size, "S", "M", "L", "XL"]
    if "size" not in st.session_state:
        st.session_state["size"] = default_size
        st.session_state["size_temp"] = default_size
    old_size = st.session_state["size"]
    if filter == 'Size':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Ukuran Produk:</div>", unsafe_allow_html=True)
        with placeholder.container():
            size_col1, size_col2, size_col3 = st.columns(3)
            with size_col1:
                def size_prev_filter():
                    size_current_index = sizes.index(st.session_state["size_temp"])
                    st.session_state["size"] = sizes[(size_current_index - 1) % len(sizes)]
                st.button("⮜", key="size_prev_filter_button", on_click=size_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with size_col2:
                st.session_state['size'] = old_size
                st.session_state['size_temp'] = old_size
                filter_size = st.selectbox(
                    "Filter Ukuran:",
                    options=sizes,
                    label_visibility="collapsed",
                    key="size"
                )
                st.session_state["size_temp"] = filter_size
                active_filters['Size'] = filter_size
            with size_col3:
                def size_next_filter():
                    size_current_index = sizes.index(st.session_state["size_temp"])
                    st.session_state["size"] = sizes[(size_current_index + 1) % len(sizes)]
                st.button("⮞", key="size_next_filter_button", on_click=size_next_filter)
    else:
        st.session_state["size"] = st.session_state["size_temp"]
        filter_size = st.session_state["size"]
        active_filters['Size'] = filter_size

    default_color = "Semua"
    colors = df['Color'].dropna().unique().tolist()
    colors.sort()
    colors.insert(0, default_color)
    if "color" not in st.session_state:
        st.session_state["color"] = default_color
        st.session_state["color_temp"] = default_color
    old_color = st.session_state["color"]
    if filter == 'Color':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Warna Produk:</div>", unsafe_allow_html=True)
        with placeholder.container():
            color_col1, color_col2, color_col3 = st.columns(3)
            with color_col1:
                def color_prev_filter():
                    color_current_index = colors.index(st.session_state["color_temp"])
                    st.session_state["color"] = colors[(color_current_index - 1) % len(colors)]
                st.button("⮜", key="color_prev_filter_button", on_click=color_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with color_col2:
                st.session_state['color'] = old_color
                st.session_state['color_temp'] = old_color
                filter_color = st.selectbox(
                    "Filter Warna:",
                    options=colors,
                    label_visibility="collapsed",
                    key="color"
                )
                st.session_state["color_temp"] = filter_color
                active_filters['Color'] = filter_color
            with color_col3:
                def color_next_filter():
                    color_current_index = colors.index(st.session_state["color_temp"])
                    st.session_state["color"] = colors[(color_current_index + 1) % len(colors)]
                st.button("⮞", key="color_next_filter_button", on_click=color_next_filter)
    else:
        st.session_state["color"] = st.session_state["color_temp"]
        filter_color = st.session_state["color"]
        active_filters['Color'] = filter_color

    default_season = "Semua"
    seasons = [default_season, "Spring", "Summer", "Fall", "Winter"]
    if "season" not in st.session_state:
        st.session_state["season"] = default_season
        st.session_state["season_temp"] = default_season
    old_season = st.session_state["season"]
    if filter == 'Season':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Musim:</div>", unsafe_allow_html=True)
        with placeholder.container():
            season_col1, season_col2, season_col3 = st.columns(3)
            with season_col1:
                def season_prev_filter():
                    season_current_index = seasons.index(st.session_state["season_temp"])
                    st.session_state["season"] = seasons[(season_current_index - 1) % len(seasons)]
                st.button("⮜", key="season_prev_filter_button", on_click=season_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with season_col2:
                st.session_state['season'] = old_season
                st.session_state['season_temp'] = old_season
                filter_season = st.selectbox(
                    "Filter Musim:",
                    options=seasons,
                    label_visibility="collapsed",
                    key="season"
                )
                st.session_state["season_temp"] = filter_season
                active_filters['Season'] = filter_season
            with season_col3:
                def season_next_filter():
                    season_current_index = seasons.index(st.session_state["season_temp"])
                    st.session_state["season"] = seasons[(season_current_index + 1) % len(seasons)]
                st.button("⮞", key="season_next_filter_button", on_click=season_next_filter)
    else:
        st.session_state["season"] = st.session_state["season_temp"]
        filter_season = st.session_state["season"]
        active_filters['Season'] = filter_season

    min_rating, max_rating = float(df['Review Rating'].min()), float(df['Review Rating'].max())
    if "range_rating" not in st.session_state:
        st.session_state["range_rating"] = (min_rating, max_rating)
        st.session_state["range_rating_temp"] = (min_rating, max_rating)
    if filter == 'Review Rating':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Rentang Rating Produk:</div>", unsafe_allow_html=True)
        with placeholder.container():
            range_rating = st.slider(
                "Filter Rating:",
                min_rating, max_rating,
                value=st.session_state["range_rating"],
                label_visibility="collapsed",
            )
            st.session_state["range_rating_temp"] = range_rating
            active_filters['Review Rating'] = f"{range_rating[0]} - {range_rating[1]}"
            if active_filters['Review Rating'] == f"{min_rating} - {max_rating}":
                active_filters['Review Rating'] = "Semua"
    else:
        st.session_state["range_rating"] = st.session_state["range_rating_temp"]
        range_rating = st.session_state["range_rating"]
        active_filters['Review Rating'] = f"{range_rating[0]} - {range_rating[1]}"
        if active_filters['Review Rating'] == f"{min_rating} - {max_rating}":
            active_filters['Review Rating'] = "Semua"

    default_subscription = "Semua"
    subscriptions = [default_subscription, "Yes", "No"]
    if "subscription" not in st.session_state:
        st.session_state["subscription"] = default_subscription
        st.session_state["subscription_temp"] = default_subscription
    old_subscription = st.session_state["subscription"]
    if filter == 'Subscription Status':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Status Berlangganan:</div>", unsafe_allow_html=True)
        with placeholder.container():
            subscription_col1, subscription_col2, subscription_col3 = st.columns(3)
            with subscription_col1:
                def subscription_prev_filter():
                    subscription_current_index = subscriptions.index(st.session_state["subscription_temp"])
                    st.session_state["subscription"] = subscriptions[(subscription_current_index - 1) % len(subscriptions)]
                st.button("⮜", key="subscription_prev_filter_button", on_click=subscription_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with subscription_col2:
                st.session_state['subscription'] = old_subscription
                st.session_state['subscription_temp'] = old_subscription
                filter_subscription = st.selectbox(
                    "Filter Status Berlangganan:",
                    options=subscriptions,
                    label_visibility="collapsed",
                    key="subscription"
                )
                st.session_state["subscription_temp"] = filter_subscription
                active_filters['Subscription Status'] = filter_subscription
            with subscription_col3:
                def subscription_next_filter():
                    subscription_current_index = subscriptions.index(st.session_state["subscription_temp"])
                    st.session_state["subscription"] = subscriptions[(subscription_current_index + 1) % len(subscriptions)]
                st.button("⮞", key="subscription_next_filter_button", on_click=subscription_next_filter)
    else:
        st.session_state["subscription"] = st.session_state["subscription_temp"]
        filter_subscription = st.session_state["subscription"]
        active_filters['Subscription Status'] = filter_subscription

    default_payment = "Semua"
    payments = df['Payment Method'].dropna().unique().tolist()
    payments.sort()
    payments.insert(0, default_payment)
    if "payment" not in st.session_state:
        st.session_state["payment"] = default_payment
        st.session_state["payment_temp"] = default_payment
    old_payment = st.session_state["payment"]
    if filter == 'Payment Method':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Metode Pembayaran:</div>", unsafe_allow_html=True)
        with placeholder.container():
            payment_col1, payment_col2, payment_col3 = st.columns(3)
            with payment_col1:
                def payment_prev_filter():
                    payment_current_index = payments.index(st.session_state["payment_temp"])
                    st.session_state["payment"] = payments[(payment_current_index - 1) % len(payments)]
                st.button("⮜", key="payment_prev_filter_button", on_click=payment_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with payment_col2:
                st.session_state['payment'] = old_payment
                st.session_state['payment_temp'] = old_payment
                filter_payment = st.selectbox(
                    "Filter Metode Pembayaran:",
                    options=payments,
                    label_visibility="collapsed",
                    key="payment"
                )
                st.session_state["payment_temp"] = filter_payment
                active_filters['Payment Method'] = filter_payment
            with payment_col3:
                def payment_next_filter():
                    payment_current_index = payments.index(st.session_state["payment_temp"])
                    st.session_state["payment"] = payments[(payment_current_index + 1) % len(payments)]
                st.button("⮞", key="payment_next_filter_button", on_click=payment_next_filter)
    else:
        st.session_state["payment"] = st.session_state["payment_temp"]
        filter_payment = st.session_state["payment"]
        active_filters['Payment Method'] = filter_payment

    default_shipping = "Semua"
    shippings = df['Shipping Type'].dropna().unique().tolist()
    shippings.sort()
    shippings.insert(0, default_shipping)
    if "shipping" not in st.session_state:
        st.session_state["shipping"] = default_shipping
        st.session_state["shipping_temp"] = default_shipping
    old_shipping = st.session_state["shipping"]
    if filter == 'Shipping Type':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Jenis Pengiriman Produk:</div>", unsafe_allow_html=True)
        with placeholder.container():
            shipping_col1, shipping_col2, shipping_col3 = st.columns(3)
            with shipping_col1:
                def shipping_prev_filter():
                    shipping_current_index = shippings.index(st.session_state["shipping_temp"])
                    st.session_state["shipping"] = shippings[(shipping_current_index - 1) % len(shippings)]
                st.button("⮜", key="shipping_prev_filter_button", on_click=shipping_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with shipping_col2:
                st.session_state['shipping'] = old_shipping
                st.session_state['shipping_temp'] = old_shipping
                filter_shipping = st.selectbox(
                    "Filter Jenis Pengiriman:",
                    options=shippings,
                    label_visibility="collapsed",
                    key="shipping"
                )
                st.session_state["shipping_temp"] = filter_shipping
                active_filters['Shipping Type'] = filter_shipping
            with shipping_col3:
                def shipping_next_filter():
                    shipping_current_index = shippings.index(st.session_state["shipping_temp"])
                    st.session_state["shipping"] = shippings[(shipping_current_index + 1) % len(shippings)]
                st.button("⮞", key="shipping_next_filter_button", on_click=shipping_next_filter)
    else:
        st.session_state["shipping"] = st.session_state["shipping_temp"]
        filter_shipping = st.session_state["shipping"]
        active_filters['Shipping Type'] = filter_shipping

    default_discount = "Semua"
    discounts = [default_discount, "Yes", "No"]
    if "discount" not in st.session_state:
        st.session_state["discount"] = default_discount
        st.session_state["discount_temp"] = default_discount
    old_discount = st.session_state["discount"]
    if filter == 'Discount Applied':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Diskon Diterapkan Pada Pembelian:</div>", unsafe_allow_html=True)
        with placeholder.container():
            discount_col1, discount_col2, discount_col3 = st.columns(3)
            with discount_col1:
                def discount_prev_filter():
                    discount_current_index = discounts.index(st.session_state["discount_temp"])
                    st.session_state["discount"] = discounts[(discount_current_index - 1) % len(discounts)]
                st.button("⮜", key="discount_prev_filter_button", on_click=discount_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with discount_col2:
                st.session_state['discount'] = old_discount
                st.session_state['discount_temp'] = old_discount
                filter_discount = st.selectbox(
                    "Filter Diskon Diterapkan:",
                    options=discounts,
                    label_visibility="collapsed",
                    key="discount"
                )
                st.session_state["discount_temp"] = filter_discount
                active_filters['Discount Applied'] = filter_discount
            with discount_col3:
                def discount_next_filter():
                    discount_current_index = discounts.index(st.session_state["discount_temp"])
                    st.session_state["discount"] = discounts[(discount_current_index + 1) % len(discounts)]
                st.button("⮞", key="discount_next_filter_button", on_click=discount_next_filter)
    else:
        st.session_state["discount"] = st.session_state["discount_temp"]
        filter_discount = st.session_state["discount"]
        active_filters['Discount Applied'] = filter_discount

    default_promotion = "Semua"
    promotions = [default_promotion, "Yes", "No"]
    if "promotion" not in st.session_state:
        st.session_state["promotion"] = default_promotion
        st.session_state["promotion_temp"] = default_promotion
    old_promotion = st.session_state["promotion"]
    if filter == 'Promo Code Used':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Kode Promosi Digunakan Pada Pembelian:</div>", unsafe_allow_html=True)
        with placeholder.container():
            promotion_col1, promotion_col2, promotion_col3 = st.columns(3)
            with promotion_col1:
                def promotion_prev_filter():
                    promotion_current_index = promotions.index(st.session_state["promotion_temp"])
                    st.session_state["promotion"] = promotions[(promotion_current_index - 1) % len(promotions)]
                st.button("⮜", key="promotion_prev_filter_button", on_click=promotion_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with promotion_col2:
                st.session_state['promotion'] = old_promotion
                st.session_state['promotion_temp'] = old_promotion
                filter_promotion = st.selectbox(
                    "Filter Kode Promosi Digunakan:",
                    options=promotions,
                    label_visibility="collapsed",
                    key="promotion"
                )
                st.session_state["promotion_temp"] = filter_promotion
                active_filters['Promo Code Used'] = filter_promotion
            with promotion_col3:
                def promotion_next_filter():
                    promotion_current_index = promotions.index(st.session_state["promotion_temp"])
                    st.session_state["promotion"] = promotions[(promotion_current_index + 1) % len(promotions)]
                st.button("⮞", key="promotion_next_filter_button", on_click=promotion_next_filter)
    else:
        st.session_state["promotion"] = st.session_state["promotion_temp"]
        filter_promotion = st.session_state["promotion"]
        active_filters['Promo Code Used'] = filter_promotion

    min_previous_purchase, max_previous_purchase = int(df['Previous Purchases'].min()), int(df['Previous Purchases'].max())
    if "range_previous_purchase" not in st.session_state:
        st.session_state["range_previous_purchase"] = (min_previous_purchase, max_previous_purchase)
        st.session_state["range_previous_purchase_temp"] = (min_previous_purchase, max_previous_purchase)
    if filter == 'Previous Purchases':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Rentang Jumlah Pembelian Pelanggan Sebelumnya:</div>", unsafe_allow_html=True)
        with placeholder.container():
            range_previous_purchase = st.slider(
                "Filter Pembelian Sebelumnya:",
                min_previous_purchase, max_previous_purchase,
                value=st.session_state["range_previous_purchase"],
                label_visibility="collapsed",
            )
            st.session_state["range_previous_purchase_temp"] = range_previous_purchase
            active_filters['Previous Purchases'] = f"{range_previous_purchase[0]} - {range_previous_purchase[1]}"
            if active_filters['Previous Purchases'] == f"{min_previous_purchase} - {max_previous_purchase}":
                active_filters['Previous Purchases'] = "Semua"
    else:
        st.session_state["range_previous_purchase"] = st.session_state["range_previous_purchase_temp"]
        range_previous_purchase = st.session_state["range_previous_purchase"]
        active_filters['Previous Purchases'] = f"{range_previous_purchase[0]} - {range_previous_purchase[1]}"
        if active_filters['Previous Purchases'] == f"{min_previous_purchase} - {max_previous_purchase}":
            active_filters['Previous Purchases'] = "Semua"

    default_preferred_payment = "Semua"
    preferred_payments = df['Preferred Payment Method'].dropna().unique().tolist()
    preferred_payments.sort()
    preferred_payments.insert(0, default_preferred_payment)
    if "preferred_payment" not in st.session_state:
        st.session_state["preferred_payment"] = default_preferred_payment
        st.session_state["preferred_payment_temp"] = default_preferred_payment
    old_preferred_payment = st.session_state["preferred_payment"]
    if filter == 'Preferred Payment Method':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Metode Pembayaran Yang Disukai Pelanggan:</div>", unsafe_allow_html=True)
        with placeholder.container():
            preferred_payment_col1, preferred_payment_col2, preferred_payment_col3 = st.columns(3)
            with preferred_payment_col1:
                def preferred_payment_prev_filter():
                    preferred_payment_current_index = preferred_payments.index(st.session_state["preferred_payment_temp"])
                    st.session_state["preferred_payment"] = preferred_payments[(preferred_payment_current_index - 1) % len(preferred_payments)]
                st.button("⮜", key="preferred_payment_prev_filter_button", on_click=preferred_payment_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with preferred_payment_col2:
                st.session_state['preferred_payment'] = old_preferred_payment
                st.session_state['preferred_payment_temp'] = old_preferred_payment
                filter_preferred_payment = st.selectbox(
                    "Filter Metode Pembayaran Yang Disukai:",
                    options=preferred_payments,
                    label_visibility="collapsed",
                    key="preferred_payment"
                )
                st.session_state["preferred_payment_temp"] = filter_preferred_payment
                active_filters['Preferred Payment Method'] = filter_preferred_payment
            with preferred_payment_col3:
                def preferred_payment_next_filter():
                    preferred_payment_current_index = preferred_payments.index(st.session_state["preferred_payment_temp"])
                    st.session_state["preferred_payment"] = preferred_payments[(preferred_payment_current_index + 1) % len(preferred_payments)]
                st.button("⮞", key="preferred_payment_next_filter_button", on_click=preferred_payment_next_filter)
    else:
        st.session_state["preferred_payment"] = st.session_state["preferred_payment_temp"]
        filter_preferred_payment = st.session_state["preferred_payment"]
        active_filters['Preferred Payment Method'] = filter_preferred_payment

    default_frequency = "Semua"
    frequencies = df['Frequency of Purchases'].dropna().unique().tolist()
    frequencies.sort()
    frequencies.insert(0, default_frequency)
    if "frequency" not in st.session_state:
        st.session_state["frequency"] = default_frequency
        st.session_state["frequency_temp"] = default_frequency
    old_frequency = st.session_state["frequency"]
    if filter == 'Frequency of Purchases':
        placeholder_title.markdown(f"<div style='margin-top: -25px; margin-bottom: -10px; font-size: 23px; color: white; text-align: center;'>Filter Frekuensi Pembelian Pelanggan:</div>", unsafe_allow_html=True)
        with placeholder.container():
            frequency_col1, frequency_col2, frequency_col3 = st.columns(3)
            with frequency_col1:
                def frequency_prev_filter():
                    frequency_current_index = frequencies.index(st.session_state["frequency_temp"])
                    st.session_state["frequency"] = frequencies[(frequency_current_index - 1) % len(frequencies)]
                st.button("⮜", key="frequency_prev_filter_button", on_click=frequency_prev_filter)
                st.markdown("<span class='tombol-kiri-detail-filter' style='display:none;'></span>", unsafe_allow_html=True)
            with frequency_col2:
                st.session_state['frequency'] = old_frequency
                st.session_state['frequency_temp'] = old_frequency
                filter_frequency = st.selectbox(
                    "Filter Frekuensi Pembelian:",
                    options=frequencies,
                    label_visibility="collapsed",
                    key="frequency"
                )
                st.session_state["frequency_temp"] = filter_frequency
                active_filters['Frequnecy of Purchases'] = filter_frequency
            with frequency_col3:
                def frequency_next_filter():
                    frequency_current_index = frequencies.index(st.session_state["frequency_temp"])
                    st.session_state["frequency"] = frequencies[(frequency_current_index + 1) % len(frequencies)]
                st.button("⮞", key="frequency_next_filter_button", on_click=frequency_next_filter)
    else:
        st.session_state["frequency"] = st.session_state["frequency_temp"]
        filter_frequency = st.session_state["frequency"]
        active_filters['Frequency of Purchases'] = filter_frequency

    df_filter = df[
        (df['Age'].between(range_usia[0], range_usia[1])) &
        ((filter_gender == default_gender) or (df['Gender'] == filter_gender)) &
        ((filter_item == default_item) or (df['Item Purchased'] == filter_item)) &
        ((filter_category == default_category) or (df['Category'] == filter_category)) &
        (df['Purchase Amount (USD)'].between(range_purchase[0], range_purchase[1])) &
        ((filter_location == default_location) or (df['Location'] == filter_location)) &
        ((filter_size == default_size) or (df['Size'] == filter_size)) &
        ((filter_color == default_color) or (df['Color'] == filter_color)) &
        ((filter_season == default_season) or (df['Season'] == filter_season)) &
        (df['Review Rating'].between(range_rating[0], range_rating[1])) &
        ((filter_subscription == default_subscription) or (df['Subscription Status'] == filter_subscription)) &
        ((filter_payment == default_payment) or (df['Payment Method'] == filter_payment)) &
        ((filter_shipping == default_shipping) or (df['Shipping Type'] == filter_shipping)) &
        ((filter_discount == default_discount) or (df['Discount Applied'] == filter_discount)) &
        ((filter_promotion == default_promotion) or (df['Promo Code Used'] == filter_promotion)) &
        (df['Previous Purchases'].between(range_previous_purchase[0], range_previous_purchase[1])) &
        ((filter_preferred_payment == default_preferred_payment) or (df['Preferred Payment Method'] == filter_preferred_payment)) &
        ((filter_frequency == default_frequency) or (df['Frequency of Purchases'] == filter_frequency))
    ]

    count_active_filters = len([filter for filter in active_filters if active_filters[filter] != "Semua"])
    if count_active_filters:
        
        kolom_filter = []
        kolom_nilai = []
        for filter in active_filters:
            if active_filters[filter] != "Semua":
                kolom_filter.append(filter)
                kolom_nilai.append(active_filters[filter])
        tabel_filter = {
            "Variabel" : kolom_filter,
            "Filter" : kolom_nilai
        }
        st.markdown(f"<div style='margin-top: -20px; display: flex; justify-content: space-between;'> \
            <div style='font-size: 29px; font-weight: bold; color: white'>Filter Diterapkan Pada Dataset</div> \
            <div style='font-size: 23px; color: white; padding-top: 10px;' ><span style='color:yellow; font-weight:bold;'>{count_active_filters}</span> Filter</div> \
            </div>", unsafe_allow_html=True)
        df_table_filter = pd.DataFrame(tabel_filter)
        df_table_filter.index = range(1, len(df_table_filter)+1)
        st.dataframe(df_table_filter)

        def reset_filter():
            st.session_state["range_slider"] = (min_usia, max_usia)
            st.session_state["range_slider_temp"] = (min_usia, max_usia)
            st.session_state["gender"] = default_gender
            st.session_state["gender_temp"] = default_gender
            st.session_state["item"] = default_item
            st.session_state["item_temp"] = default_item
            st.session_state["category"] = default_category
            st.session_state["category_temp"] = default_category
            st.session_state["range_purchase"] = (min_purchase, max_purchase)
            st.session_state["range_purchase_temp"] = (min_purchase, max_purchase)
            st.session_state["location"] = default_location
            st.session_state["location_temp"] = default_location
            st.session_state["size"] = default_size
            st.session_state["size_temp"] = default_size
            st.session_state["color"] = default_color
            st.session_state["color_temp"] = default_color
            st.session_state["season"] = default_season
            st.session_state["season_temp"] = default_season
            st.session_state["range_rating"] = (min_rating, max_rating)
            st.session_state["range_rating_temp"] = (min_rating, max_rating)
            st.session_state["subscription"] = default_subscription
            st.session_state["subscription_temp"] = default_subscription
            st.session_state["payment"] = default_payment
            st.session_state["payment_temp"] = default_payment
            st.session_state["shipping"] = default_shipping
            st.session_state["shipping_temp"] = default_shipping
            st.session_state["discount"] = default_discount
            st.session_state["discount_temp"] = default_discount
            st.session_state["promotion"] = default_discount
            st.session_state["promotion_temp"] = default_discount
            st.session_state["range_previous_purchase"] = (min_previous_purchase, max_previous_purchase)
            st.session_state["range_previous_purchase_temp"] = (min_previous_purchase, max_previous_purchase)
            st.session_state["preferred_payment"] = default_preferred_payment
            st.session_state["preferred_payment_temp"] = default_preferred_payment
            st.session_state["frequency"] = default_preferred_payment
            st.session_state["frequency_temp"] = default_preferred_payment
            st.session_state["filter"] = default_filter_option
        st.button("Reset Filter", on_click=reset_filter) 

        st.markdown(f"<div style='height: 20px;'></div>", unsafe_allow_html=True)

    if len(df_filter) != len(df):
        teks = "Subset"
        warna = "yellow"
    else:
        teks = "Dataset"
        warna = "white"
    st.markdown(f"<div style='margin-top: -20px; display: flex; justify-content: space-between;'> \
        <div style='font-size: 29px; font-weight: bold; color: {warna}'>{teks}</div> \
        <div style='font-size: 23px; color: white; padding-top: 10px;' ><span style='color:{warna}; font-weight:bold;'>{len(df_filter)}</span> Transaksi</div> \
        </div>", unsafe_allow_html=True)
    df_filter.index = range(1, len(df_filter)+1)
    st.dataframe(df_filter)
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

    st.markdown(f"<div style='margin-top: -9px; display: flex; justify-content: space-between;'> \
        <div style='font-size: 29px; font-weight: bold; color: white'>Visualisasi Data</div> \
        </div>", unsafe_allow_html=True)

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
        )
        if len(top_10_items) == 1:
            fig.update_traces(marker_color=random.choice(["#2EABB8", "#845B53", "#C03D3E", "#7F7F7F", "#E1812C", "#9372B2", "#3A923A", "#A9AA35", "#D684BD", "#3274A1"]))
        else:
            fig.update_traces(marker_color=["#2EABB8", "#845B53", "#C03D3E", "#7F7F7F", "#E1812C", "#9372B2", "#3A923A", "#A9AA35", "#D684BD", "#3274A1"])
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
        category_dict_colors = {
            "Accessories": "#C03D3E",
            "Clothing": "#3274A1",
            "Footwear": "#E1812C",
            "Outerwear": "#3A923A"
        }
        category_colors = list(map(lambda x:category_dict_colors[x], df_categories["Kategori Produk"].to_list()))
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
            marker_color=category_colors,
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
        if len(top_locations) == 1:
            fig.update_traces(marker_color=random.choice(["#E1812C", "#A9AA35", "#845B53", "#3A923A", "#2EABB8", "#C03D3E", "#D684BD", "#7F7F7F", "#9372B2", "#3274A1"]))
        else:
            fig.update_traces(marker_color=["#E1812C", "#A9AA35", "#845B53", "#3A923A", "#2EABB8", "#C03D3E", "#D684BD", "#7F7F7F", "#9372B2", "#3274A1"])
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
        size_counts = df_filter["Size"].value_counts().reindex(size_order).reset_index().dropna()
        size_counts.columns = ["Ukuran Produk", "Frekuensi Pembelian"]
        size_dict_colors = {
            "S": "#E1812C",
            "M": "#3A923A",
            "L": "#3274A1",
            "XL": "#C03D3E"
        }
        size_colors = list(map(lambda x:size_dict_colors[x], size_counts["Ukuran Produk"].to_list()))
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
            marker_color=size_colors
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

    if pilihan == "Color":
        top_10_colors = df_filter["Color"].value_counts().head(10)[::-1]
        list_color = top_10_colors.index.to_list()
        df_top10 = top_10_colors.reset_index()
        df_top10.columns = ["Warna Produk", "Frekuensi Pembelian"]
        color_dict_colors = {
            "Gold": "#FFD700",
            "Brown": "#A52A2A",
            "White": "#FFFFFF",
            "Turquoise": "#40E0D0",
            "Lavender": "#E6E6FA",
            "Indigo": "#4B0082",
            "Beige": "#F5F5DC",
            "Red": "#FF0000",
            "Peach": "#FFE5B4",
            "Purple": "#800080",
            "Magenta": "#FF00FF",
            "Blue": "#0000FF",
            "Pink": "#FFC0CB",
            "Charcoal": "#36454F",
            "Orange": "#FFA500",
            "Maroon": "#800000",
            "Gray": "#808080",
            "Violet": "#EE82EE",
            "Cyan": "#00FFFF",
            "Black": "#000000",
            "Green": "#008000",
            "Teal": "#008080",
            "Silver": "#C0C0C0",
            "Yellow": "#FFFF00",
            "Olive": "#808000",
        }
        color_colors = list(map(lambda x:color_dict_colors[x], df_top10["Warna Produk"].to_list()))
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
            marker_color=color_colors,
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
        try:
            y_max = max([max(trace.y) for trace in fig.data if hasattr(trace, "y")])
        except:
            y_max = 0
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
        status_counts = df_filter["Subscription Status"].value_counts().reindex(status_order).reset_index().dropna()
        status_counts.columns = ["Status Berlangganan", "Jumlah Pelanggan"]
        subscription_dict_colors = {
            "Yes": "#3274A1",
            "No": "#E1812C"
        }
        subscription_colors = list(map(lambda x:subscription_dict_colors[x], status_counts["Status Berlangganan"].to_list()))

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
            marker_color=subscription_colors
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
        try:
            y_max = max([max(trace.y) for trace in fig.data if hasattr(trace, "y")])
        except:
            y_max = 0
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
            marker=dict(colors=subscription_colors),
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Payment Method":
        top_methods = df_filter["Payment Method"].value_counts()[::-1]
        df_methods = top_methods.reset_index()
        df_methods.columns = ["Metode Pembayaran", "Jumlah Transaksi"]
        methods_dict_colors = {
            "Credit Card": "#3274A1",
            "Venmo": "#9372B2",
            "Cash": "#3A923A",
            "PayPal": "#C03D3E",
            "Debit Card": "#845B53",
            "Bank Transfer": "#E1812C"
        }
        methods_colors = list(map(lambda x:methods_dict_colors[x], df_methods["Metode Pembayaran"].to_list()))
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
            marker_color=methods_colors,
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
        shippings_dict_colors = {
            "Free Shipping": "#E1812C",
            "Standard": "#C03D3E",
            "Store Pickup": "#845B53",
            "Next Day Air": "#3A923A",
            "Express": "#3274A1",
            "2-Day Shipping": "#9372B2"
        }
        shipping_colors = list(map(lambda x:shippings_dict_colors[x], df_shippings["Jenis Pengiriman"].to_list()))
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
            marker_color=shipping_colors,
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
        discounts_counts = df_filter["Discount Applied"].value_counts().reindex(discounts_order).reset_index().dropna()
        discounts_counts.columns = ["Diskon Diterapkan", "Frekuensi Pembelian"]
        discounts_dict_colors = {
            "Yes": "#3274A1",
            "No": "#E1812C"
        }
        discount_colors = list(map(lambda x:discounts_dict_colors[x], discounts_counts["Diskon Diterapkan"].to_list()))

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
            marker_color=discount_colors
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
        try:
            y_max = max([max(trace.y) for trace in fig.data if hasattr(trace, "y")])
        except:
            y_max = 0
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
            marker=dict(colors=discount_colors),
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Promo Code Used":
        promo_order = ["Yes", "No"]
        promo_counts = df_filter["Promo Code Used"].value_counts().reindex(promo_order).reset_index().dropna()
        promo_counts.columns = ["Kode Promosi Digunakan", "Frekuensi Pembelian"]
        promo_dict_colors = {
            "Yes": "#3274A1",
            "No": "#E1812C"
        }
        promo_colors = list(map(lambda x:promo_dict_colors[x], promo_counts["Kode Promosi Digunakan"].to_list()))

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
            marker_color=promo_colors
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
        try:
            y_max = max([max(trace.y) for trace in fig.data if hasattr(trace, "y")])
        except:
            y_max = 0
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
            marker=dict(colors=promo_colors),
        )
        fig.update_layout(
            title=dict(x=0.5, xanchor="center", font=dict(size=30, color="black")),
            showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Previous Purchases":
        min_pembelian = df_filter["Previous Purchases"].min()
        max_pembelian = df_filter["Previous Purchases"].max() + 1
        size_pembelian = (max_pembelian - min_pembelian)//10
        if (max_pembelian - min_pembelian)%10 > 0:
            size_pembelian = size_pembelian + 1
        fig = px.histogram(df_filter, x="Previous Purchases", labels={"Previous Purchases": "Jumlah Pembelian Sebelumnya",
            "count": "Jumlah Pelanggan"}, height=600, title="Distribusi Jumlah Pembelian Pelanggan Sebelumnya") 
        fig.update_traces(
            xbins=dict(
                start=min_pembelian,
                end=max_pembelian,
                size=size_pembelian
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
        fig.update_xaxes(tickfont=dict(color="black", size=14), range=[min_pembelian-5, max_pembelian+5])
        fig.update_yaxes(tickfont=dict(color="black", size=14))
        if df_filter.empty:
            fig.update_xaxes(range=[0, 10])
            fig.update_yaxes(range=[0, 10])        
        st.plotly_chart(fig, use_container_width=True)

    if pilihan == "Preferred Payment Method":
        top_methods = df_filter["Preferred Payment Method"].value_counts()[::-1]
        df_methods = top_methods.reset_index()
        df_methods.columns = ["Metode Pembayaran Yang Disukai", "Jumlah Pelanggan"]
        methods_dict_colors = {
            "PayPal": "#C03D3E",
            "Credit Card": "#3A923A",
            "Cash": "#E1812C",
            "Debit Card": "#845B53",
            "Venmo": "#3274A1",
            "Bank Transfer": "#9372B2"
        }
        methods_colors = list(map(lambda x:methods_dict_colors[x], df_methods["Metode Pembayaran Yang Disukai"].to_list()))
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
            marker_color=methods_colors,
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
        purchases_dict_colors = {
            "Every 3 Months": "#D684BD",
            "Annually": "#3A923A",
            "Quarterly": "#C03D3E",
            "Monthly": "#C03D3E",
            "Bi-Weekly": "#9372B2",
            "Fortnightly": "#3274A1",
            "Weekly": "#E1812C"
        }
        purchases_colors = list(map(lambda x:purchases_dict_colors[x], df_purchases["Frekuensi Pembelian"].to_list()))
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
            marker_color=purchases_colors,
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
