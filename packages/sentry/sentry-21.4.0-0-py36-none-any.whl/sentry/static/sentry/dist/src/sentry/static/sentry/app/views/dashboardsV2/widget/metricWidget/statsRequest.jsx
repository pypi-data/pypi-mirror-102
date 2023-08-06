import { __assign, __read, __spreadArray } from "tslib";
import { useEffect, useState } from 'react';
import pick from 'lodash/pick';
import { addErrorMessage } from 'app/actionCreators/indicator';
import { getParams } from 'app/components/organizations/globalSelectionHeader/getParams';
import { URL_PARAM } from 'app/constants/globalSelectionHeader';
import { t } from 'app/locale';
import { fillChartDataFromSessionsResponse, getInterval, } from 'app/views/releases/detail/overview/chart/utils';
import { roundDuration } from 'app/views/releases/utils';
import { getBreakdownChartData } from './utils';
function StatsRequest(_a) {
    var api = _a.api, organization = _a.organization, projectId = _a.projectId, queries = _a.queries, environments = _a.environments, datetime = _a.datetime, location = _a.location, children = _a.children, yAxis = _a.yAxis;
    var _b = __read(useState(false), 2), isLoading = _b[0], setIsLoading = _b[1];
    var _c = __read(useState(false), 2), errored = _c[0], setErrored = _c[1];
    var _d = __read(useState([]), 2), series = _d[0], setSeries = _d[1];
    useEffect(function () {
        fetchData();
    }, [projectId, environments, datetime, queries, yAxis]);
    function fetchData() {
        if (!yAxis) {
            return;
        }
        var queriesWithAggregation = queries.filter(function (_a) {
            var aggregation = _a.aggregation;
            return !!aggregation;
        });
        if (!queriesWithAggregation.length) {
            return;
        }
        setIsLoading(true);
        var promises = queriesWithAggregation.map(function (_a) {
            var aggregation = _a.aggregation, groupBy = _a.groupBy;
            return api.requestPromise("/organizations/" + organization.slug + "/sessions/", {
                query: __assign({ project: projectId, environment: environments, groupBy: groupBy || null, field: aggregation + "(" + yAxis + ")", interval: getInterval(datetime) }, getParams(pick(location.query, Object.values(URL_PARAM)))),
            });
        });
        Promise.all(promises)
            .then(function (results) {
            getChartData(results);
        })
            .catch(function (error) {
            var _a, _b;
            addErrorMessage((_b = (_a = error.responseJSON) === null || _a === void 0 ? void 0 : _a.detail) !== null && _b !== void 0 ? _b : t('Error loading chart data'));
            setErrored(true);
        });
    }
    function getChartData(sessionReponses) {
        if (!sessionReponses.length || !yAxis) {
            return;
        }
        var seriesData = sessionReponses.map(function (sessionReponse, index) {
            var _a = queries[index], aggregation = _a.aggregation, groupBy = _a.groupBy;
            var field = aggregation + "(" + yAxis + ")";
            var breakDownChartData = getBreakdownChartData({
                response: sessionReponse,
                groupBy: groupBy || null,
            });
            var chartData = fillChartDataFromSessionsResponse({
                response: sessionReponse,
                field: field,
                groupBy: groupBy || null,
                chartData: breakDownChartData,
                valueFormatter: yAxis === 'session.duration'
                    ? function (duration) { return roundDuration(duration ? duration / 1000 : 0); }
                    : undefined,
            });
            return __spreadArray([], __read(Object.values(chartData)));
        });
        var newSeries = seriesData.reduce(function (mergedSeries, chartDataSeries) {
            return mergedSeries.concat(chartDataSeries);
        }, []);
        setSeries(newSeries);
        setIsLoading(false);
    }
    return children({ isLoading: isLoading, errored: errored, series: series });
}
export default StatsRequest;
//# sourceMappingURL=statsRequest.jsx.map