---
created: 2025-03-11T12:51:25 (UTC +01:00)
tags: []
source: https://desktop.arcgis.com/en/arcmap/latest/get-started/installation-guide/uninstalling.htm
author: 
---
# Uninstalling ArcGIS Desktop—ArcMap | Documentation

> ## Excerpt
> Refer to the following for guidance on uninstalling previous ArcGIS products.

---
-   [Uninstalling ArcGIS Desktop products](https://desktop.arcgis.com/en/arcmap/latest/get-started/installation-guide/uninstalling.htm#GUID-914BA229-3DAA-4C32-8E39-899423A7059A)
-   [Uninstalling Python](https://desktop.arcgis.com/en/arcmap/latest/get-started/installation-guide/uninstalling.htm#ESRI_SECTION1_2687B0D4689443D79561E7CA0877077D)
-   [How to perform an uninstallation of ArcGIS Desktop silently](https://desktop.arcgis.com/en/arcmap/latest/get-started/installation-guide/uninstalling.htm#ESRI_SECTION1_5A3562353C60436893C9AAFB19B9583C)
-   [How to perform an uninstallation of ArcGIS Desktop language packs silently](https://desktop.arcgis.com/en/arcmap/latest/get-started/installation-guide/uninstalling.htm#ESRI_SECTION1_721995B8505042BD881ECCC5BF7AA8FE)

The ArcGIS software components can be easily uninstalled. Regardless of the software product type installed, the Add/Remove program item will be listed as ArcGIS Desktop.

Selecting ArcGIS Desktop 10.8.2 from the Add/Remove Programs dialog box provides the option to uninstall (Remove All) or add and remove installation components. For information on adding or removing installation components, see [Adding ArcGIS Desktop installation components](https://desktop.arcgis.com/en/arcmap/latest/get-started/installation-guide/adding-additional-installation-components.htm).

## Uninstalling ArcGIS Desktop products

1.  Click Start \> Control Panel and then Programs and Features
2.  Select Programs > ArcGIS Desktop 10.8.2.
3.  Select Remove to uninstall ArcGIS Desktop from your machine.

To uninstall ArcGIS Desktop language packs, follow the steps above. Instead of selecting ArcGIS Desktop 10.8.2, select the ArcGIS Desktop language pack that you want to remove. If multiple ArcGIS Desktoplanguage packs are installed, each language pack must be uninstalled separately.

## Uninstalling Python

When Python is installed by the ArcGIS Desktop setup, it will be uninstalled when you uninstall ArcGIS Desktop.

## How to perform an uninstallation of ArcGIS Desktop silently

To uninstall a product silently, use the following Windows Installer command:

msiexec /x <{product code}> /qb

For example, to uninstall ArcGIS Desktop 10.8.2 silently, use the following command line:

msiexec.exe /x {791AB03F-1AF2-43FE-8F5D-8FDC9509D7CF} /qb

## How to perform an uninstallation of ArcGIS Desktop language packs silently

To uninstall ArcGIS Desktop language packs silently, replace the above product code with the product code of the language pack to be uninstalled. Language pack product codes are listed in the table below:

<table><colgroup width="*"></colgroup><colgroup width="*"></colgroup><tbody><tr><td outputclass="" rowspan="1" colspan="1"><p id="GUID-9FE7E0C1-E814-4EBC-8831-7952D887188D">ArcGIS for Desktop Arabic language pack</p></td><td outputclass="" rowspan="1" colspan="1"><p id="GUID-B580D74E-D39F-4B2E-A101-B9689D2A6EB7">{94F0E0BE-F23C-4B83-AD48-F491C664F4AB}</p></td></tr><tr><td outputclass="" rowspan="1" colspan="1"><p id="GUID-A6A1AC60-91A5-460F-BD74-1495AA1FFBA2">ArcGIS for Desktop Chinese language pack</p></td><td outputclass="" rowspan="1" colspan="1"><p id="GUID-F6A1C834-B370-411C-9791-2EF9F3BF5B64">{8666D126-46B7-426A-879F-B2CF60AE70D2}</p></td></tr><tr><td outputclass="" rowspan="1" colspan="1"><p id="GUID-88735B74-9E48-45BB-9F99-BC60E01EE262">ArcGIS for Desktop Finnish language pack</p></td><td outputclass="" rowspan="1" colspan="1"><p id="GUID-72CD3152-74CE-4125-BAC5-9B5C0475CB18">{BFA774EA-1B33-48C7-80A5-775A61430566}</p></td></tr><tr><td outputclass="" rowspan="1" colspan="1"><p id="GUID-502FBAA3-D255-469B-8D2A-F81E23DAE628">ArcGIS for Desktop French language pack</p></td><td outputclass="" rowspan="1" colspan="1"><p id="GUID-8F7AE922-7EFA-40E5-B891-4F565D6CD962">{2B2F83D1-1C9C-44AB-9BBC-37412F057D2F}</p></td></tr><tr><td outputclass="" rowspan="1" colspan="1"><p id="GUID-20809D8A-8BD7-479D-A9D0-1EE1A1447555">ArcGIS for Desktop German language pack</p></td><td outputclass="" rowspan="1" colspan="1"><p id="GUID-2A6D66C3-E741-420B-806C-71AFDF3BDDD5">{04B36F74-40CF-403B-AA7A-AB4FE8166F95}</p></td></tr><tr><td outputclass="" rowspan="1" colspan="1"><p id="GUID-EF0E19E8-FD38-4A84-B0D9-A7BADF250A53">ArcGIS for Desktop Italian language pack</p></td><td outputclass="" rowspan="1" colspan="1"><p id="GUID-76019052-37D7-4E3C-876F-3DB3C89BE1F4">{3B575A31-03E3-4845-A519-02ABC96DC1B1}</p></td></tr><tr><td outputclass="" rowspan="1" colspan="1"><p id="GUID-974F2329-E908-4D27-8914-057F6958CB4D">ArcGIS for Desktop Japanese language pack</p></td><td outputclass="" rowspan="1" colspan="1"><p id="GUID-2CFC5197-941E-4B2F-9476-09B3715F47DD">{4FCC9BE3-7150-49E8-983D-389FC46F8676}</p></td></tr><tr><td outputclass="" rowspan="1" colspan="1"><p id="GUID-AF4E788D-7007-4F81-A998-7F2D0C88EAC6">ArcGIS for Desktop Brazilian Portuguese language pack</p></td><td outputclass="" rowspan="1" colspan="1"><p id="GUID-10254C4B-4B8B-44F7-9BD5-368998F21354">{58D6B3BC-91A7-430B-B86D-EE8D07C772FD}</p></td></tr><tr><td outputclass="" rowspan="1" colspan="1"><p id="GUID-4FE72E61-1C9C-4E28-8EF6-1E48D8A4C245">ArcGIS for Desktop Russian language pack</p></td><td outputclass="" rowspan="1" colspan="1"><p id="GUID-4E9C2A2B-9BE7-4C2D-B993-5F0BC561B5A6">{ 642BDDAE-2295-44C4-9FC1-99A01C7FEF72}</p></td></tr><tr><td outputclass="" rowspan="1" colspan="1"><p id="GUID-FEEA2BEC-0B52-426B-924C-86D42AE330E9">ArcGIS for Desktop Spanish language pack</p></td><td outputclass="" rowspan="1" colspan="1"><p id="GUID-CCCB7E1C-1517-4FAB-8CD1-88FF8BCB2CE9">{1EC6D79A-C3EB-4CFE-9193-D310A0382A2A}</p></td></tr><tr><td outputclass="" rowspan="1" colspan="1"><p id="GUID-B98339A1-94EA-4953-B6E5-9CB2179118C6">ArcGIS for Desktop Turkish language pack</p></td><td outputclass="" rowspan="1" colspan="1"><p id="GUID-DB1AEC03-358B-4079-99F9-D96207305FF2">{7F76BB78-1FEF-441E-8B90-4196FEA5DD64}</p></td></tr></tbody><caption></caption></table>

Any ArcGIS product can be uninstalled silently using the product code.
