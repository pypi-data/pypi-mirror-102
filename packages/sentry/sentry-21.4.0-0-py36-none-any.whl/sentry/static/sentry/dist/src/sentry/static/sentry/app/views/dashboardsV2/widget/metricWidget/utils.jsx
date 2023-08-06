export function getBreakdownChartData(_a) {
    var response = _a.response, groupBy = _a.groupBy;
    return response.groups.reduce(function (groups, group, index) {
        var seriesName = groupBy ? group.by[groupBy] : index;
        groups[seriesName] = {
            seriesName: seriesName,
            data: [],
        };
        return groups;
    }, {});
}
//# sourceMappingURL=utils.jsx.map