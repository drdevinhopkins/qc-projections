from datetime import date
# from get_qc_predictions import *
from get_qc_data import *
import altair as alt
import streamlit as st
import numpy as np

from streamlit import caching
caching.clear_cache()

st.beta_set_page_config(page_title=None, page_icon=None, layout='wide', initial_sidebar_state='auto')

today = pd.to_datetime(date.today())

# st.markdown(hide_menu_style, unsafe_allow_html=True)


qc_data, region_data_df, mtl_data_df, mtl_ed_df, qc_ed_stretcher_df = load_qc_data()
arrondissement_df = load_arrondissement_data()
mtl_courbe_df = load_mtl_courbe()
# total_cases_projections, total_deaths_projections = load_qc_projections()

# st.title('Quebec EDs')

# prefer_log = st.checkbox('Log scale', False)
# if prefer_log:
#     scale = alt.Scale(base=10, type='log')
# else:
#     scale = alt.Scale(type='linear')
prefer_log = False


# total_cases_data = pd.concat(
#     [qc_data[['date', 'total_cases']], total_cases_projections])
# # source2 = source1.set_index('date').round(1).reset_index()
# # source2 = source2.reset_index(drop=True).melt(
# #     'date', var_name='category', value_name='y')

# # The basic line
# line1 = alt.Chart(total_cases_data).mark_line().encode(
#     x=alt.X('monthdate(date)', title='Date'),
#     y=alt.Y('total_cases:Q', title='Total Cases'
#             )
# )
# line2 = alt.Chart(total_cases_data).mark_line(strokeDash=[1, 1]).encode(
#     x=alt.X('monthdate(date)', title='Date'),
#     y=alt.Y('realistic:Q', title='Total Cases')
# )

# area = line2.mark_area(opacity=0.3).encode(
#     alt.Y('optimistic:Q', title='Total Cases',
#           scale=scale),
#     alt.Y2('pessimistic:Q', title='Total Cases')
# )

# total_cases_chart = alt.layer(
#     line1, line2, area
# ).interactive()

# st.altair_chart(total_cases_chart, use_container_width=True)

# total_deaths_data = pd.concat(
#     [qc_data[['date', 'total_deaths']], total_deaths_projections[total_deaths_projections.date > today]])

# # st.table(total_deaths_data)
# # source2 = source1.set_index('date').round(1).reset_index()
# # source2 = source2.reset_index(drop=True).melt(
# #     'date', var_name='category', value_name='y')

# # The basic line
# real_deaths_line = alt.Chart(total_deaths_data).mark_line().encode(
#     x=alt.X('monthdate(date)', title='Date'),
#     y=alt.Y('total_deaths:Q', title='Total Deaths'
#             )
# )
# # line2 = alt.Chart(total_cases_data).mark_line(strokeDash=[1, 1]).encode(
# #     x=alt.X('monthdate(date)', title='Date'),
# #     y=alt.Y('realistic:Q', title='Total Cases')
# # )

# predicted_deaths_area = real_deaths_line.mark_area(opacity=0.3).encode(
#     alt.Y('optimistic:Q', title='Total Deaths',
#           scale=scale),
#     alt.Y2('pessimistic:Q', title='Total Deaths')
# )

# total_deaths_chart = alt.layer(
#     real_deaths_line, predicted_deaths_area
# ).interactive()

# st.altair_chart(total_deaths_chart, use_container_width=True)

# # realistic_pred_chart = alt.Chart(realistic).mark_line(strokeDash=[1, 1]).encode(
# #     x='monthdate(date)',
# #     y='total_cases'
# # )
# # optimistic_pred_chart = alt.Chart(optimistic).mark_line(strokeDash=[1, 1]).encode(
# #     x='monthdate(date)',
# #     y='total_cases'
# # )
# # pessimistic_pred_chart = alt.Chart(pessimistic).mark_line(strokeDash=[1, 1]).encode(
# #     x='monthdate(date)',
# #     y='total_cases'
# # )
# # real_total_case_chart = alt.Chart(qc_data[['date', 'total_cases']]).mark_line().encode(
# #     x='monthdate(date)',
# #     y='total_cases'
# # )

# # st.altair_chart(real_total_case_chart + realistic_pred_chart +
# #                 optimistic_pred_chart + pessimistic_pred_chart, use_container_width=True)
# # st.header("Current Situation")

# # choose_log = st.checkbox('Log scale', True)
# # if choose_log:
# #     qc_total_case1 = alt.Chart(qc_data).transform_fold(
# #         ['total_case'],
# #         as_=['measure', 'number']
# #     ).mark_line(point=True).encode(
# #         x='monthdate(date)',
# #         y=alt.Y('number:Q', scale=alt.Scale(base=10, type='log'),
# #                 axis=alt.Axis(orient='left')),
# #         color='measure:N',
# #         tooltip=['date', 'measure:N', 'number:Q']
# #     ).interactive()
# #     qc_total_case2 = alt.Chart(qc_data.replace(0, np.nan).dropna()).transform_fold(
# #         ['total_recovered'],
# #         as_=['measure', 'number']
# #     ).mark_line(point=True).encode(
# #         x='monthdate(date)',
# #         y=alt.Y('number:Q', scale=alt.Scale(base=10, type='log'),
# #                 axis=alt.Axis(orient='left')),
# #         color='measure:N',
# #         tooltip=['date', 'measure:N', 'number:Q']
# #     ).interactive()
# #     qc_total_case = qc_total_case1 + qc_total_case2
# # else:
# #     qc_total_case = alt.Chart(qc_data[['date', 'total_case', 'total_recovered']]).transform_fold(
# #         ['total_case', 'total_recovered'],
# #         as_=['measure', 'number']
# #     ).mark_line(point=True).encode(
# #         x='monthdate(date)',
# #         y='number:Q',
# #         color='measure:N',
# #         tooltip=['date', 'measure:N', 'number:Q']
# #     ).configure_legend(orient="right").interactive()
# # st.altair_chart(qc_total_case, use_container_width=True)

# # if choose_log:
# #     qc_death_hosp_icu = alt.Chart(qc_data.replace(0, np.nan).dropna()).transform_fold(
# #         ['total_death', 'hospitalisations', 'ICU'],
# #         as_=['measure', 'number']
# #     ).mark_line(point=True).encode(
# #         x='monthdate(date)',
# #         y=alt.Y('number:Q', scale=alt.Scale(base=10, type='log'),
# #                 axis=alt.Axis(orient='left')),
# #         color='measure:N',
# #         tooltip=['date', 'measure:N', 'number:Q']
# #     ).configure_legend(orient="right").interactive()
# # else:
# #     qc_death_hosp_icu = alt.Chart(qc_data).transform_fold(
# #         ['total_death', 'hospitalisations', 'ICU'],
# #         as_=['measure', 'number']
# #     ).mark_line(point=True).encode(
# #         x='monthdate(date)',
# #         y='number:Q',
# #         color='measure:N',
# #         tooltip=['date', 'measure:N', 'number:Q']
# #     ).configure_legend(orient="right").interactive()
# # st.altair_chart(qc_death_hosp_icu, use_container_width=True)

# selected_regions = st.multiselect(
#     'Total cases by region(s)', region_data_df.region.unique().tolist(),
#     default=['Montréal', 'Montérégie', 'Laval', 'Lanaudière'])
# # default=region_data_df.region.unique().tolist())
# regions_chart = alt.Chart(region_data_df[region_data_df.region.isin(selected_regions)].dropna()).mark_line(point=True).encode(
#     x='monthdate(date)',
#     y='total_case',
#     color='region',
#     tooltip=['date', 'region', 'total_case']
# ).interactive()  # .configure_legend(orient="bottom")
# st.altair_chart(regions_chart, use_container_width=True)

# selected_arrondissement = st.multiselect(
#     'Total cases by Montreal neighbourhood', mtl_data_df.arrondissement.unique().tolist(), default=['Côte-Saint-Luc', 'Outremont', 'Hampstead', 'LaSalle', 'Côte-des-Neiges–Notre-Dame-de-Grâce'])
# mtl_chart = alt.Chart(mtl_data_df[mtl_data_df.arrondissement.isin(selected_arrondissement)].dropna()).mark_line(point=True).encode(
#     x='monthdate(date)',
#     y='total_case',
#     color='arrondissement',
#     tooltip=['date', 'arrondissement', 'total_case']
# ).interactive()  # .configure_legend(orient="bottom")
# st.altair_chart(mtl_chart, use_container_width=True)

# hospital_visit_slider = st.slider(
#     'Days to display: ', min_value=7, max_value=90, value=14)
selected_hospital_visits = st.multiselect('Montreal Emergency Department Visits', mtl_ed_df.Installation.unique().tolist(), default=[
    "L'Hôpital général juif Sir Mortimer B. Davis", "Centre hospitalier de St. Mary", "Hôpital Royal Victoria", "Hôpital général de Montréal", 'Hôpital général du Lakeshore'])
mtl_chart = alt.Chart(mtl_ed_df[mtl_ed_df.Installation.isin(selected_hospital_visits)].dropna()).mark_line(point=True).encode(
    # x='monthdate(date)',
    x='date',
    y='Nombre inscriptions',
    color='Installation',
    tooltip=['date', 'Installation', 'Nombre inscriptions']
).interactive()  # .configure_legend(orient="bottom")
st.altair_chart(mtl_chart, use_container_width=True)

st.subheader('Emergency Department Stretcher Occupancy')
selected_hospital_stretchers = st.multiselect('Emergency Departments', qc_ed_stretcher_df.installation.unique().tolist(), default=[
    "L'Hôpital général Juif Sir Mortimer B. Davis", "Centre hospitalier de St. Mary", "Hôpital Royal Victoria", "Hôpital général de Montréal"])
stretcher_chart = alt.Chart(qc_ed_stretcher_df[qc_ed_stretcher_df.installation.isin(selected_hospital_stretchers)].dropna()).mark_line(point=True).encode(
    x="timestamp",
    y='occupied',
    color='installation',
    tooltip=[
        "timestamp", 'installation', 'occupied']
).interactive()  # .configure_legend(orient="bottom")
st.altair_chart(stretcher_chart, use_container_width=True)

st.subheader('Total cases by Montreal neighbourhood')
selected_arrondissement = st.multiselect(
    'Montreal Neighbourhoods',
    arrondissement_df.arrondissement.unique().tolist(), default=['Côte-Saint-Luc', 'Outremont', 'Hampstead', 'Côte-des-Neiges–Notre-Dame-de-Grâce', 'Westmount'])
mtl_chart = alt.Chart(arrondissement_df[arrondissement_df.arrondissement.isin(selected_arrondissement)]).mark_line(point=True).encode(
    x='monthdate(date)',
    y='total_case',
    color='arrondissement',
    tooltip=['date', 'arrondissement', 'total_case']
).interactive()  # .configure_legend(orient="bottom")
st.altair_chart(mtl_chart, use_container_width=True)

# st.table(mtl_courbe_df)

st.subheader('Montreal New Cases')
mtl_new_cases = alt.Chart(mtl_courbe_df).mark_line(point=True).encode(
    # x='monthdate(date)',
    x='monthdate(date)',
    y='new_cases',
    tooltip=['date', 'new_cases']
).interactive()  # .configure_legend(orient="bottom")
st.altair_chart(mtl_new_cases, use_container_width=True)

st.subheader('Montreal Total Cases')
mtl_total_cases = alt.Chart(mtl_courbe_df).mark_line(point=False).encode(
    # x='monthdate(date)',
    x='monthdate(date)',
    y='total_cases',
    tooltip=['date', 'total_cases']
).interactive()  # .configure_legend(orient="bottom")
st.altair_chart(mtl_total_cases, use_container_width=True)