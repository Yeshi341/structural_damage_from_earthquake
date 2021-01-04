The data for the three datasets used are described below. The data information comes from [here](https://eq2015.npc.gov.np/#/download)

## Building Use Dataset

| Feature | Type | Description|
|-------- | ----- | ---------- |
| building_id | Text | A unique ID that identifies every individual building |
| district_id | Text | District where the building is located |
| vdcmun_id | Text | Municipality where the building is located |
| ward_id | Text | Ward Number in which the building is located |
| legal_ownership_status | Categorical |Legal ownership status of the land in which the building was built |
| count_families | Number |Number of families in the building |
| has_secondary_use | Boolean |Flag variable that indicates if the building is used for any secondary purpose |
| has_secondary_use_agriculture | Boolean |Flag variable that indicates if the building is secondarily used for agricultural purpose |
| has_secondary_use_hotel | Boolean | Flag variable that indicates if the building is secondarily used as hotel |
| has_secondary_use_rental | Boolean | Flag variable that indicates if the building is secondarily used for rental purpose |
| has_secondary_use_institution| Boolean | Flag variable that indicates if the building is secondarily used for institutional purpose |
| has_secondary_use_school | Boolean | Flag variable that indicates if the building is secondarily used as school |
| has_secondary_use_industry | Boolean | Flag variable that indicates if the building is secondarily used for industrial purpose |
| has_secondary_use_health_post | Boolean | Flag variable that indicates if the building is secondarily used as health post |
| has_secondary_use_gov_office | Boolean | Flag variable that indicates if the building is secondarily used as government office |
| has_secondary_use_use_police | Boolean | Flag variable that indicates if the building is secondarily used as police station |
| has_secondary_use_other | Boolean | Flag variable that indicates if the building is secondarily used for other purpose |
| id | Number | A unique ID that identifies a unique information from all table |

## Building Structure Dataset

| Feature | Type | Description |
| ------- | ---- | ----------- |
| building_id | Text | A unique ID that identifies a unique building from the survey |
| district_id | Text | District where the building is located |
| vdcmun_id | Text | Municipality where the building is located | 
| ward_id | Text | Ward Number in which the building is located |
| count_floors_pre_eq | Number | Number of floors that the building had before the earthquake |
| count_floors_post_eq | Number | Number of floors that the building had after the earthquake |
| age_building | Number | Age of the building (in years) |
| plinth_area_sq_ft | Number | Plinth area of the building (in square feet) |
| height_ft_pre_eq | Number | Height of the building before the earthquake (in feet) |
| height_ft_post_eq | Number | Height of the building after the earthquake (in feet) |
| land_surface_condition | Categorical | Surface condition of the land in which the building is built |
| foundation_type | Categorical | Type of foundation used in the building |
| roof_type | Categorical | Type of roof used in the building |
| ground_floor_type | Categorical |Ground floor type |
| other_floor_type | Categorical | Type of construction used in other floors (except ground floor and roof) |
| position | Categorical | Position of the building |
| plan_configuration | Categorical | Building plan configuration |
| has_superstructure_adobe_mud | Boolean |Flag variable that indicates if the superstructure of the building is made of Adobe/Mud |
| has_superstructure_mud_mortar_stone | Boolean | Flag variable that indicates if the superstructure of the building is made of Mud Mortar - Stone |
| has_superstructure_stone_flag | Boolean | Flag variable that indicates if the superstructure of the building is made of Stone |
| has_superstructure_cement_mortar_stone | Boolean | Flag variable that indicates if the superstructure of the building is made of Stone |
| has_superstructure_mud_mortar_brick | Boolean | Flag variable that indicates if the superstructure of the building is made of Cement Mortar - Stone |
| has_superstructure_cement_mortar_brick | Boolean | Flag variable that indicates if the superstructure of the building is made of Mud Mortar - Brick |
| has_superstructure_timber | Boolean | Flag variable that indicates if the superstructure of the building is made of Timber |
| has_superstructure_bamboo | Boolean | Flag variable that indicates if the superstructure of the building is made of Bamboo |
| has_superstructure_rc_non_engineered | Boolean | Flag variable that indicates if the superstructure of the building is made of RC (Non Engineered) |
| has_superstructure_rc_engineered | Boolean | Flag variable that indicates if the superstructure of the building is made of RC (Engineered) |
| has_superstructure_other | Boolean | Flag variable that indicates if the superstructure of the building is made of any other material |
| condition_post_eq | Categorical | Actual contition of the building after the earthquake |
| damage_grade | Categorical | Damage grade assigned to the building by the surveyor after assessment |
| technical_solution_proposed | Categorical | Technical solution proposed by the surveyor after assessment |
| id | Number | A unique ID that identifies a unique information from all table |

## Building Damage Assessment Dataset

| Feature | Type | Description |
| ------- | ---- | ----------- |
| building_id | Text | A unique ID that identifies every individual building in the survey |
district_id | Text | District where the building is located |
vdcmun_id | Text | Municipality where the building is located |
ward_id | Text | Ward Number in which the building is located |
has_geotechnical_risk | Text | Flag variable that indicates if the building has geotechnical risk |
has_geotechnical_risk_land_settlement | Text |Flag variable that indicates if the building has geotechnical risks related to land settlement |
has_geotechnical_risk_fault_crack | Text | Flag variable that indicates if the building has geotechnical risks related to fault cracking |
has_geotechnical_risk_liquefaction | Text | Flag variable that indicates if the building has geotechnical risks related to liquefaction |
has_geotechnical_risk_landslide | Boolean | Flag variable that indicates if the building has risk geotechnical risks related to landslide |
has_geotechnical_risk_rock_fall | Boolean | Flag variable that indicates if the building has geotechnical risk related to rockfall |
has_geotechnical_risk_flood | Boolean | Flag variable that indicates if the building has geotechnical risks related to flood |
has_geotechnical_risk_other | Boolean | Flag variable that indicates if the building has any other geotechnical risk |
id | Number | A unique ID that identifies a unique information from all table |
