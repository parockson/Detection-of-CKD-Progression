SELECT
    "Revenue"."Sales_Daily_ActualsVrsTarget"."Week" AS "Week",
    "Revenue"."Sales_Daily_ActualsVrsTarget"."Biz Segment" AS "Biz Segment",
    "Revenue"."Sales_Daily_ActualsVrsTarget"."Category Alias" AS "Category Alias",
    "Revenue"."Sales_Daily_ActualsVrsTarget"."Month" AS "Month",
    sum(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Transactional Value"
    ) AS "Actuals Value",
    sum(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Transactional Volume"
    ) AS "Actuals Volume",
    sum(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Gross Margin"
    ) AS "Actuals Gross Margin",
    sum(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Net Margin"
    ) AS "Actuals Net Margin",
    sum(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Daily Target Transactional Value"
    ) AS "Taget Value",
    sum(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Daily Target Transactional Volume"
    ) AS "Target Volume",
    sum(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Daily Target Gross Margin"
    ) AS "Target Gross  Margin",
    sum(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Daily Target Net Margin"
    ) AS "Target Net Margin",
    max(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Target Transactional Value"
    ) AS "Target Month Value",
    max(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Target Transactional Volume"
    ) AS "Target Month Volume",
    max(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Target Gross Margin"
    ) AS "Target Month Gross Margin",
    max(
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Target Net Margin"
    ) AS "Target Month Net Margin"
FROM
    "Revenue"."Sales_Daily_ActualsVrsTarget"
WHERE
    (
        "Revenue"."Sales_Daily_ActualsVrsTarget"."Time_Created" >= DateFromParts (year (getdate ()), month (getdate ()), 1)
        AND "Revenue"."Sales_Daily_ActualsVrsTarget"."Time_Created" < DateFromParts (
            year (dateadd (month, 1, getdate ())),
            month (dateadd (month, 1, getdate ())),
            1
        )
    )
GROUP BY
    "Revenue"."Sales_Daily_ActualsVrsTarget"."Week",
    "Revenue"."Sales_Daily_ActualsVrsTarget"."Biz Segment",
    "Revenue"."Sales_Daily_ActualsVrsTarget"."Category Alias",
    "Revenue"."Sales_Daily_ActualsVrsTarget"."Month"
ORDER BY
    "Revenue"."Sales_Daily_ActualsVrsTarget"."Week" ASC,
    "Revenue"."Sales_Daily_ActualsVrsTarget"."Biz Segment" ASC,
    "Revenue"."Sales_Daily_ActualsVrsTarget"."Category Alias" ASC,
    -- "Revenue"."Sales_Daily_ActualsVrsTarget"."Month" ASC