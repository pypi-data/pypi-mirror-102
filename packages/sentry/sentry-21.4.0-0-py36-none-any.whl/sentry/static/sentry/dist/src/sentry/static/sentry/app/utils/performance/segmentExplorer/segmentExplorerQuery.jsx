import React from 'react';
import GenericDiscoverQuery from 'app/utils/discover/genericDiscoverQuery';
import withApi from 'app/utils/withApi';
export function getRequestFunction(_props) {
    var tagOrder = _props.tagOrder, aggregateColumn = _props.aggregateColumn;
    function getTagExplorerRequestPayload(props) {
        var eventView = props.eventView;
        var apiPayload = eventView.getEventsAPIPayload(props.location);
        apiPayload.order = tagOrder;
        apiPayload.aggregateColumn = aggregateColumn;
        return apiPayload;
    }
    return getTagExplorerRequestPayload;
}
function shouldRefetchData(prevProps, nextProps) {
    return (prevProps.tagOrder !== nextProps.tagOrder ||
        prevProps.aggregateColumn !== nextProps.aggregateColumn);
}
function afterFetch(data) {
    var newData = data;
    return newData.map(function (row) {
        var firstItem = row.topValues[0];
        row.tagValue = firstItem;
        row.aggregate = firstItem.aggregate;
        row.frequency = firstItem.count;
        row.comparison = firstItem.comparison;
        row.otherValues = row.topValues.slice(0);
        var otherEventValue = row.topValues.reduce(function (acc, curr) { return acc - curr.count; }, 1);
        if (otherEventValue > 0.01) {
            row.otherValues.push({
                name: 'other',
                value: 'other',
                isOther: true,
                aggregate: 0,
                count: otherEventValue,
                comparison: 0,
            });
        }
        return row;
    });
}
function SegmentExplorerQuery(props) {
    return (<GenericDiscoverQuery route="events-facets-performance" getRequestPayload={getRequestFunction(props)} shouldRefetchData={shouldRefetchData} afterFetch={afterFetch} {...props}/>);
}
export default withApi(SegmentExplorerQuery);
//# sourceMappingURL=segmentExplorerQuery.jsx.map