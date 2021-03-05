import csv
import numpy as np
import matplotlib.pyplot as plt

def Avarage(lst):
    return sum(lst) / len(lst)

with open('/home/ruben/Downloads/ppp_output.csv', 'r') as csv_file:
    read1 = csv.reader(csv_file, delimiter=",")

    AUS_list_m = [0]
    AUS_list_f = [0]
    AUS_list_other = [0]

    AUT_list_m = [0]
    AUT_list_f = [0]
    AUT_list_other = [0]

    BEL_list_m = [0]
    BEL_list_f = [0]
    BEL_list_other = [0]

    CAN_list_m = [0]
    CAN_list_f = [0]
    CAN_list_other = [0]

    CZE_list_m = [0]
    CZE_list_f = [0]
    CZE_list_other = [0]

    DNK_list_m = [0]
    DNK_list_f = [0]
    DNK_list_other = [0]

    FIN_list_m = [0]
    FIN_list_f = [0]
    FIN_list_other = [0]

    FRA_list_m = [0]
    FRA_list_f = [0]
    FRA_list_other = [0]

    DEU_list_m = [0]
    DEU_list_f = [0]
    DEU_list_other = [0]

    GRC_list_m = [0]
    GRC_list_f = [0]
    GRC_list_other = [0]

    HUN_list_m = [0]
    HUN_list_f = [0]
    HUN_list_other = [0]

    IRL_list_m = [0]
    IRL_list_f = [0]
    IRL_list_other = [0]

    ITA_list_m = [0]
    ITA_list_f = [0]
    ITA_list_other = [0]

    JPN_list_m = [0]
    JPN_list_f = [0]
    JPN_list_other = [0]

    KOR_list_m = [0]
    KOR_list_f = [0]
    KOR_list_other = [0]

    LUX_list_m = [0]
    LUX_list_f = [0]
    LUX_list_other = [0]

    NLD_list_m = [0]
    NLD_list_f = [0]
    NLD_list_other = [0]

    NOR_list_m = [0]
    NOR_list_f = [0]
    NOR_list_other = [0]

    POL_list_m = [0]
    POL_list_f = [0]
    POL_list_other = [0]

    PRT_list_m = [0]
    PRT_list_f = [0]
    PRT_list_other = [0]

    SVK_list_m = [0]
    SVK_list_f = [0]
    SVK_list_other = [0]

    ESP_list_m = [0]
    ESP_list_f = [0]
    ESP_list_other = [0]

    SWE_list_m = [0]
    SWE_list_f = [0]
    SWE_list_other = [0]


    CHE_list_m = [0]
    CHE_list_f = [0]
    CHE_list_other = [0]

    GBR_list_m = [0]
    GBR_list_f = [0]
    GBR_list_other = [0]

    USA_list_m = [0]
    USA_list_f = [0]
    USA_list_other = [0]

    MEX_list_m = [0]
    MEX_list_f = [0]
    MEX_list_other = [0]

    ISR_list_m = [0]
    ISR_list_f = [0]
    ISR_list_other = [0]

    SVN_list_m = [0]
    SVN_list_f = [0]
    SVN_list_other = [0]

    EST_list_m = [0]
    EST_list_f = [0]
    EST_list_other = [0]

    ISL_list_m = [0]
    ISL_list_f = [0]
    ISL_list_other = [0]

    NZL_list_m = [0]
    NZL_list_f = [0]
    NZL_list_other = [0]

    CHL_list_m = [0]
    CHL_list_f = [0]
    CHL_list_other = [0]

    LVA_list_m = [0]
    LVA_list_f = [0]
    LVA_list_other = [0]

    LTU_list_m = [0]
    LTU_list_f = [0]
    LTU_list_other = [0]
    for row in read1:
        if row[1] == 'Australia':
            if row[11] == 'Male':
                AUS_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                AUS_list_f.append(float(row[17]))
            else:
                AUS_list_other.append(float(row[17]))
        if row[1] == 'Austria':
            if row[11] == 'Male':
                AUT_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                AUT_list_f.append(float(row[17]))
            else:
                AUT_list_other.append(float(row[17]))
        if row[1] == 'Belgium':
            if row[11] == 'Male':
                BEL_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                BEL_list_f.append(float(row[17]))
            else:
                BEL_list_other.append(float(row[17]))
        if row[1] == 'Canada':
            if row[11] == 'Male':
                CAN_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                CAN_list_f.append(float(row[17]))
            else:
                CAN_list_other.append(float(row[17]))
        if row[1] == 'Czech Republic':
            if row[11] == 'Male':
                CZE_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                CZE_list_f.append(float(row[17]))
            else:
                CZE_list_other.append(float(row[17]))
        if row[1] == 'Denmark':
            if row[11] == 'Male':
                DNK_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                DNK_list_f.append(float(row[17]))
            else:
                DNK_list_other.append(float(row[17]))
        if row[1] == 'Finland':
            if row[11] == 'Male':
                FIN_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                FIN_list_f.append(float(row[17]))
            else:
                FIN_list_other.append(float(row[17]))
        if row[1] == 'France':
            if row[11] == 'Male':
                FRA_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                FRA_list_f.append(float(row[17]))
            else:
                FRA_list_other.append(float(row[17]))
        if row[1] == 'Germany':
            if row[11] == 'Male':
                DEU_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                DEU_list_f.append(float(row[17]))
            else:
                DEU_list_other.append(float(row[17]))
        if row[1] == 'Greece':
            if row[11] == 'Male':
                GRC_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                GRC_list_f.append(float(row[17]))
            else:
                GRC_list_other.append(float(row[17]))
        if row[1] == 'Hungary':
            if row[11] == 'Male':
                HUN_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                HUN_list_f.append(float(row[17]))
            else:
                HUN_list_other.append(float(row[17]))
        if row[1] == 'Ireland':
            if row[11] == 'Male':
                IRL_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                IRL_list_f.append(float(row[17]))
            else:
                IRL_list_other.append(float(row[17]))
        if row[1] == 'Italy':
            if row[11] == 'Male':
                ITA_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                ITA_list_f.append(float(row[17]))
            else:
                ITA_list_other.append(float(row[17]))
        if row[1] == 'Japan':
            if row[11] == 'Male':
                JPN_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                JPN_list_f.append(float(row[17]))
            else:
                JPN_list_other.append(float(row[17]))
        if row[1] == 'Republic of Korea':
            if row[11] == 'Male':
                KOR_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                KOR_list_f.append(float(row[17]))
            else:
                KOR_list_other.append(float(row[17]))
        if row[1] == 'Netherlands':
            if row[11] == 'Male':
                NLD_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                NLD_list_f.append(float(row[17]))
            else:
                NLD_list_other.append(float(row[17]))
        if row[1] == 'Norway':
            if row[11] == 'Male':
                NOR_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                NOR_list_f.append(float(row[17]))
            else:
                NOR_list_other.append(float(row[17]))
        if row[1] == 'Poland':
            if row[11] == 'Male':
                POL_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                POL_list_f.append(float(row[17]))
            else:
                POL_list_other.append(float(row[17]))
        if row[1] == 'Portugal':
            if row[11] == 'Male':
                PRT_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                PRT_list_f.append(float(row[17]))
            else:
                PRT_list_other.append(float(row[17]))
        if row[1] == 'Slovakia':
            if row[11] == 'Male':
                SVK_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                SVK_list_f.append(float(row[17]))
            else:
                SVK_list_other.append(float(row[17]))
        if row[1] == 'Spain':
            if row[11] == 'Male':
                ESP_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                ESP_list_f.append(float(row[17]))
            else:
                ESP_list_other.append(float(row[17]))
        if row[1] == 'Sweden':
            if row[11] == 'Male':
                SWE_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                SWE_list_f.append(float(row[17]))
            else:
                SWE_list_other.append(float(row[17]))
        if row[1] == 'Switzerland':
            if row[11] == 'Male':
                CHE_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                CHE_list_f.append(float(row[17]))
            else:
                CHE_list_other.append(float(row[17]))
        if row[1] == 'United Kingdom':
            if row[11] == 'Male':
                GBR_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                GBR_list_f.append(float(row[17]))
            else:
                GBR_list_other.append(float(row[17]))
        if row[1] == 'United States':
            if row[11] == 'Male':
                USA_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                USA_list_f.append(float(row[17]))
            else:
                USA_list_other.append(float(row[17]))
        if row[1] == 'Mexico':
            if row[11] == 'Male':
                MEX_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                MEX_list_f.append(float(row[17]))
            else:
                MEX_list_other.append(float(row[17]))
        if row[1] == 'Israel':
            if row[11] == 'Male':
                ISR_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                ISR_list_f.append(float(row[17]))
            else:
                ISR_list_other.append(float(row[17]))
        if row[1] == 'Slovenia':
            if row[11] == 'Male':
                SVN_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                SVN_list_f.append(float(row[17]))
            else:
                SVN_list_other.append(float(row[17]))
        if row[1] == 'Estonia':
            if row[11] == 'Male':
                EST_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                EST_list_f.append(float(row[17]))
            else:
                EST_list_other.append(float(row[17]))
        if row[1] == 'Iceland':
            if row[11] == 'Male':
                ISL_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                ISL_list_f.append(float(row[17]))
            else:
                ISL_list_other.append(float(row[17]))
        if row[1] == 'New Zealand':
            if row[11] == 'Male':
                NZL_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                NZL_list_f.append(float(row[17]))
            else:
                NZL_list_other.append(float(row[17]))
        if row[1] == 'Chile':
            if row[11] == 'Male':
                CHL_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                CHL_list_f.append(float(row[17]))
            else:
                CHL_list_other.append(float(row[17]))
        if row[1] == 'Latvia':
            if row[11] == 'Male':
                LVA_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                LVA_list_f.append(float(row[17]))
            else:
                LVA_list_other.append(float(row[17]))
        if row[1] == 'Lithuania':
            if row[11] == 'Male':
                LTU_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                LTU_list_f.append(float(row[17]))
            else:
                LTU_list_other.append(float(row[17]))
        if row[1] == 'Luxembourg':
            if row[11] == 'Male':
                LUX_list_m.append(float(row[17]))
            elif row[11] == 'Female':
                LUX_list_f.append(float(row[17]))
            else:
                LUX_list_other.append(float(row[17]))

AUS_m_average = Avarage(AUS_list_m)
AUS_f_average = Avarage(AUS_list_f)
AUS_other_average = Avarage(AUS_list_other)

print("AUS")
print(AUS_m_average)
print(AUS_f_average)
print(AUS_other_average)
print("-----")

AUT_m_average = Avarage(AUT_list_m)
AUT_f_average = Avarage(AUT_list_f)
AUT_other_average = Avarage(AUT_list_other)

print("AUT")
print(AUT_m_average)
print(AUT_f_average)
print(AUT_other_average)
print("-----")

BEL_m_average = Avarage(BEL_list_m)
BEL_f_average = Avarage(BEL_list_f)
BEL_other_average = Avarage(BEL_list_other)

print("BEL")
print(BEL_m_average)
print(BEL_f_average)
print(BEL_other_average)
print("-----")

CAN_m_average = Avarage(CAN_list_m)
CAN_f_average = Avarage(CAN_list_f)
CAN_other_average = Avarage(CAN_list_other)

print("CAN")
print(CAN_m_average)
print(CAN_f_average)
print(CAN_other_average)
print("-----")



CZE_m_average = Avarage(CZE_list_m)
CZE_f_average = Avarage(CZE_list_f)
CZE_other_average = Avarage(CZE_list_other)

print("CZE")
print(CZE_m_average)
print(CZE_f_average)
print(CZE_other_average)
print("-----")





DNK_m_average = Avarage(DNK_list_m)
DNK_f_average = Avarage(DNK_list_f)
DNK_other_average = Avarage(DNK_list_other)

print("DNK")
print(DNK_m_average)
print(DNK_f_average)
print(DNK_other_average)
print("-----")




FIN_m_average = Avarage(FIN_list_m)
FIN_f_average = Avarage(FIN_list_f)
FIN_other_average = Avarage(FIN_list_other)

print("FIN")
print(FIN_m_average)
print(FIN_f_average)
print(FIN_other_average)
print("-----")




FRA_m_average = Avarage(FRA_list_m)
FRA_f_average = Avarage(FRA_list_f)
FRA_other_average = Avarage(FRA_list_other)

print("FRA")
print(FRA_m_average)
print(FRA_f_average)
print(FRA_other_average)
print("-----")



DEU_m_average = Avarage(DEU_list_m)
DEU_f_average = Avarage(DEU_list_f)
DEU_other_average = Avarage(DEU_list_other)

print("DEU")
print(DEU_m_average)
print(DEU_f_average)
print(DEU_other_average)
print("-----")



GRC_m_average = Avarage(GRC_list_m)
GRC_f_average = Avarage(GRC_list_f)
GRC_other_average = Avarage(GRC_list_other)

print("GRC")
print(GRC_m_average)
print(GRC_f_average)
print(GRC_other_average)
print("-----")



HUN_m_average = Avarage(HUN_list_m)
HUN_f_average = Avarage(HUN_list_f)
HUN_other_average = Avarage(HUN_list_other)

print("HUN")
print(HUN_m_average)
print(HUN_f_average)
print(HUN_other_average)
print("-----")


IRL_m_average = Avarage(IRL_list_m)
IRL_f_average = Avarage(IRL_list_f)
IRL_other_average = Avarage(IRL_list_other)

print("IRL")
print(IRL_m_average)
print(IRL_f_average)
print(IRL_other_average)
print("-----")



ITA_m_average = Avarage(ITA_list_m)
ITA_f_average = Avarage(ITA_list_f)
ITA_other_average = Avarage(ITA_list_other)

print("ITA")
print(ITA_m_average)
print(ITA_f_average)
print(ITA_other_average)
print("-----")



JPN_m_average = Avarage(JPN_list_m)
JPN_f_average = Avarage(JPN_list_f)
JPN_other_average = Avarage(JPN_list_other)

print("JPN")
print(JPN_m_average)
print(JPN_f_average)
print(JPN_other_average)
print("-----")



KOR_m_average = Avarage(KOR_list_m)
KOR_f_average = Avarage(KOR_list_f)
KOR_other_average = Avarage(KOR_list_other)

print("KOR")
print(KOR_m_average)
print(KOR_f_average)
print(KOR_other_average)
print("-----")




LUX_m_average = Avarage(LUX_list_m)
LUX_f_average = Avarage(LUX_list_f)
LUX_other_average = Avarage(LUX_list_other)

print("LUX")
print(LUX_m_average)
print(LUX_f_average)
print(LUX_other_average)
print("-----")



NOR_m_average = Avarage(NOR_list_m)
NOR_f_average = Avarage(NOR_list_f)
NOR_other_average = Avarage(NOR_list_other)

print("NOR")
print(NOR_m_average)
print(NOR_f_average)
print(NOR_other_average)
print("-----")



LUX_m_average = Avarage(LUX_list_m)
LUX_f_average = Avarage(LUX_list_f)
LUX_other_average = Avarage(LUX_list_other)

print("LUX")
print(LUX_m_average)
print(LUX_f_average)
print(LUX_other_average)
print("-----")


NLD_m_average = Avarage(NLD_list_m)
NLD_f_average = Avarage(NLD_list_f)
NLD_other_average = Avarage(NLD_list_other)

print("NLD")
print(NLD_m_average)
print(NLD_f_average)
print(NLD_other_average)
print("-----")


NOR_m_average = Avarage(NOR_list_m)
NOR_f_average = Avarage(NOR_list_f)
NOR_other_average = Avarage(NOR_list_other)

print("NOR")
print(NOR_m_average)
print(NOR_f_average)
print(NOR_other_average)
print("-----")


POL_m_average = Avarage(POL_list_m)
POL_f_average = Avarage(POL_list_f)
POL_other_average = Avarage(POL_list_other)

print("POL")
print(POL_m_average)
print(POL_f_average)
print(POL_other_average)
print("-----")


PRT_m_average = Avarage(PRT_list_m)
PRT_f_average = Avarage(PRT_list_f)
PRT_other_average = Avarage(PRT_list_other)

print("PRT")
print(PRT_m_average)
print(PRT_f_average)
print(PRT_other_average)
print("-----")


SVK_m_average = Avarage(SVK_list_m)
SVK_f_average = Avarage(SVK_list_f)
SVK_other_average = Avarage(SVK_list_other)

print("SVK")
print(SVK_m_average)
print(SVK_f_average)
print(SVK_other_average)
print("-----")


ESP_m_average = Avarage(ESP_list_m)
ESP_f_average = Avarage(ESP_list_f)
ESP_other_average = Avarage(ESP_list_other)

print("ESP")
print(ESP_m_average)
print(ESP_f_average)
print(ESP_other_average)
print("-----")


SWE_m_average = Avarage(SWE_list_m)
SWE_f_average = Avarage(SWE_list_f)
SWE_other_average = Avarage(SWE_list_other)

print("SWE")
print(SWE_m_average)
print(SWE_f_average)
print(SWE_other_average)
print("-----")


CHE_m_average = Avarage(CHE_list_m)
CHE_f_average = Avarage(CHE_list_f)
CHE_other_average = Avarage(CHE_list_other)

print("CHE")
print(CHE_m_average)
print(CHE_f_average)
print(CHE_other_average)
print("-----")



GBR_m_average = Avarage(GBR_list_m)
GBR_f_average = Avarage(GBR_list_f)
GBR_other_average = Avarage(GBR_list_other)

print("GBR")
print(GBR_m_average)
print(GBR_f_average)
print(GBR_other_average)
print("-----")



USA_m_average = Avarage(USA_list_m)
USA_f_average = Avarage(USA_list_f)
USA_other_average = Avarage(USA_list_other)

print("USA")
print(USA_m_average)
print(USA_f_average)
print(USA_other_average)
print("-----")


MEX_m_average = Avarage(MEX_list_m)
MEX_f_average = Avarage(MEX_list_f)
MEX_other_average = Avarage(MEX_list_other)

print("MEX")
print(MEX_m_average)
print(MEX_f_average)
print(MEX_other_average)
print("-----")


ISR_m_average = Avarage(ISR_list_m)
ISR_f_average = Avarage(ISR_list_f)
ISR_other_average = Avarage(ISR_list_other)

print("ISR")
print(ISR_m_average)
print(ISR_f_average)
print(ISR_other_average)
print("-----")


SVN_m_average = Avarage(SVN_list_m)
SVN_f_average = Avarage(SVN_list_f)
SVN_other_average = Avarage(SVN_list_other)

print("SVN")
print(SVN_m_average)
print(SVN_f_average)
print(SVN_other_average)
print("-----")

EST_m_average = Avarage(EST_list_m)
EST_f_average = Avarage(EST_list_f)
EST_other_average = Avarage(EST_list_other)

print("EST")
print(EST_m_average)
print(EST_f_average)
print(EST_other_average)
print("-----")

ISL_m_average = Avarage(ISL_list_m)
ISL_f_average = Avarage(ISL_list_f)
ISL_other_average = Avarage(ISL_list_other)

print("ISL")
print(ISL_m_average)
print(ISL_f_average)
print(ISL_other_average)
print("-----")

NZL_m_average = Avarage(NZL_list_m)
NZL_f_average = Avarage(NZL_list_f)
NZL_other_average = Avarage(NZL_list_other)

print("NZL")
print(NZL_m_average)
print(NZL_f_average)
print(NZL_other_average)
print("-----")

CHL_m_average = Avarage(CHL_list_m)
CHL_f_average = Avarage(CHL_list_f)
CHL_other_average = Avarage(CHL_list_other)

print("CHL")
print(CHL_m_average)
print(CHL_f_average)
print(CHL_other_average)
print("-----")

LVA_m_average = Avarage(LVA_list_m)
LVA_f_average = Avarage(LVA_list_f)
LVA_other_average = Avarage(LVA_list_other)

print("LVA")
print(LVA_m_average)
print(LVA_f_average)
print(LVA_other_average)
print("-----")

LTU_m_average = Avarage(LTU_list_m)
LTU_f_average = Avarage(LTU_list_f)
LTU_other_average = Avarage(LTU_list_other)

print("LTU")
print(LTU_m_average)
print(LTU_f_average)
print(LTU_other_average)
print("-----")

data = [
    ["AUS", "AUT", "BEL", "CAN", "CZE", "DNK", "FIN",
     "FRA", "DEU", "GRC", "HUN", "IRL", "ITA", "JPN",
     "KOR", "LUX", "NLD", "NOR", "POL", "PRT", "SVK",
     "EST", "SWE", "CHE", "GBR", "USA", "MEX", "ISR",
     "SVN", "EST", "ISL", "NZL", "CHL", "LVA", "LTU"],
    [AUS_m_average, AUT_m_average, BEL_m_average, CAN_m_average, CZE_m_average, DNK_m_average, FIN_m_average,
     FRA_m_average, DEU_m_average, GRC_m_average, HUN_m_average, IRL_m_average, ITA_m_average, JPN_m_average,
     KOR_m_average, LUX_m_average, NLD_m_average, NOR_m_average, POL_m_average, PRT_m_average, SVK_m_average,
     EST_m_average, SWE_m_average, CHE_m_average, GBR_m_average, USA_m_average, MEX_m_average, ISR_m_average,
     SVN_m_average, EST_m_average, ISL_m_average, NZL_m_average, CHL_m_average, LVA_m_average, LTU_m_average],
    [AUS_f_average, AUT_f_average, BEL_f_average, CAN_f_average, CZE_f_average, DNK_f_average, FIN_f_average,
     FRA_f_average, DEU_f_average, GRC_f_average, HUN_f_average, IRL_f_average, ITA_f_average, JPN_f_average,
     KOR_f_average, LUX_f_average, NLD_f_average, NOR_f_average, POL_f_average, PRT_f_average, SVK_f_average,
     EST_f_average, SWE_f_average, CHE_f_average, GBR_f_average, USA_f_average, MEX_f_average, ISR_f_average,
     SVN_f_average, EST_f_average, ISL_f_average, NZL_f_average, CHL_f_average, LVA_f_average, LTU_f_average]

    ]


X = np.arange(35)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], width = 0.25)
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
ax.bar(X + 0.25, data[2], color = 'g', width = 0.25)
ax.set_ylabel('Avarage Salary / PPP per Gender')
ax.set_title('Avarage Salary / PPP per Gender')
#ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
plt.show()