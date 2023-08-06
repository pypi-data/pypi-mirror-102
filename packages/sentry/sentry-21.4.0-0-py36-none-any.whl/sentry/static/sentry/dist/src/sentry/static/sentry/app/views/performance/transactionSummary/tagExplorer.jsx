import { __assign, __extends, __makeTemplateObject } from "tslib";
import React from 'react';
import { browserHistory } from 'react-router';
import styled from '@emotion/styled';
import DropdownButton from 'app/components/dropdownButton';
import DropdownControl, { DropdownItem } from 'app/components/dropdownControl';
import GridEditable from 'app/components/gridEditable';
import Link from 'app/components/links/link';
import Pagination from 'app/components/pagination';
import Tooltip from 'app/components/tooltip';
import { t } from 'app/locale';
import space from 'app/styles/space';
import { formatPercentage } from 'app/utils/formatters';
import SegmentExplorerQuery from 'app/utils/performance/segmentExplorer/segmentExplorerQuery';
import { decodeScalar } from 'app/utils/queryString';
import { stringifyQueryObject, tokenizeSearch } from 'app/utils/tokenizeSearch';
import { PerformanceDuration } from '../utils';
var COLUMN_ORDER = [
    {
        key: 'key',
        name: 'Key',
        width: -1,
        column: {
            kind: 'field',
        },
    },
    {
        key: 'tagValue',
        name: 'Tag Values',
        width: -1,
        column: {
            kind: 'field',
        },
    },
    {
        key: 'frequency',
        name: 'Frequency',
        width: -1,
        column: {
            kind: 'field',
        },
    },
    {
        key: 'comparison',
        name: 'Comparison',
        width: -1,
        column: {
            kind: 'field',
        },
    },
    {
        key: 'otherValues',
        name: 'Facet Map',
        width: -1,
        column: {
            kind: 'field',
        },
    },
];
var HEADER_OPTIONS = [
    {
        label: 'Suspect Tag Values',
        value: '-sumdelta',
    },
    {
        label: 'Slowest Tag Values',
        value: '-aggregate',
    },
    {
        label: 'Fastest Tag Values',
        value: 'aggregate',
    },
];
var DURATION_OPTIONS = [
    {
        label: 'transaction.duration',
        value: 'duration',
    },
    {
        label: 'measurements.lcp',
        value: 'measurements[lcp]',
    },
];
var handleTagValueClick = function (location, tagKey, tagValue) {
    var queryString = decodeScalar(location.query.query);
    var conditions = tokenizeSearch(queryString || '');
    conditions.addTagValues(tagKey, [tagValue]);
    var query = stringifyQueryObject(conditions);
    browserHistory.push({
        pathname: location.pathname,
        query: __assign(__assign({}, location.query), { query: String(query).trim() }),
    });
};
var renderBodyCell = function (parentProps, column, dataRow) {
    var value = dataRow[column.key];
    var location = parentProps.location;
    if (column.key === 'tagValue') {
        var localValue_1 = dataRow.tagValue;
        return (<Link to="" onClick={function () { return handleTagValueClick(location, dataRow.key, localValue_1.value); }}>
        <TagValue value={localValue_1}/>
      </Link>);
    }
    if (column.key === 'frequency') {
        var localValue = dataRow.frequency;
        return formatPercentage(localValue, 0);
    }
    if (column.key === 'comparison') {
        var localValue = dataRow.comparison;
        var text = '';
        if (localValue > 1) {
            var pct = formatPercentage(localValue - 1, 0);
            text = "+" + pct + " slower";
        }
        else {
            var pct = formatPercentage(localValue - 1, 0);
            text = pct + " faster";
        }
        return (<Tooltip title={PerformanceDuration({ milliseconds: dataRow.aggregate })}>
        {t(text)}
      </Tooltip>);
    }
    if (column.key === 'otherValues' && Array.isArray(value)) {
        var converted = dataRow.otherValues;
        var segments = converted.map(function (val) {
            return {
                count: val.count,
                name: val.name,
                key: dataRow.key,
                value: val.value,
                isOther: val.isOther,
                url: '',
            };
        });
        return <SegmentVisualization location={location} segments={segments}/>;
    }
    return value;
};
var SegmentVisualization = function (props) {
    var location = props.location, segments = props.segments;
    return (<SegmentBar>
      {segments.map(function (value, index) {
            var pct = value.count * 100;
            var pctLabel = Math.floor(pct);
            var renderTooltipValue = function () {
                return value.name || t('n/a');
            };
            var tooltipHtml = (<React.Fragment>
            <div className="truncate">{renderTooltipValue()}</div>
            {pctLabel}%
          </React.Fragment>);
            var segmentProps = {
                index: index,
                to: value.url,
                onClick: function () { var _a; return handleTagValueClick(location, (_a = value.key) !== null && _a !== void 0 ? _a : '', value.value); },
            };
            return (<div key={value.value} style={{ width: pct + '%' }}>
            <Tooltip title={tooltipHtml} containerDisplayMode="block">
              {value.isOther ? <OtherSegment /> : <Segment {...segmentProps}/>}
            </Tooltip>
          </div>);
        })}
    </SegmentBar>);
};
var SegmentBar = styled('div')(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  display: flex;\n  overflow: hidden;\n  border-radius: 2px;\n"], ["\n  display: flex;\n  overflow: hidden;\n  border-radius: 2px;\n"])));
var COLORS = [
    '#3A3387',
    '#5F40A3',
    '#8C4FBD',
    '#B961D3',
    '#DE76E4',
    '#EF91E8',
    '#F7B2EC',
    '#FCD8F4',
    '#FEEBF9',
];
var OtherSegment = styled('span')(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  display: block;\n  width: 100%;\n  height: 16px;\n  color: inherit;\n  outline: none;\n  background-color: ", ";\n"], ["\n  display: block;\n  width: 100%;\n  height: 16px;\n  color: inherit;\n  outline: none;\n  background-color: ", ";\n"])), COLORS[COLORS.length - 1]);
var Segment = styled(Link)(templateObject_3 || (templateObject_3 = __makeTemplateObject(["\n  display: block;\n  width: 100%;\n  height: 16px;\n  color: inherit;\n  outline: none;\n  background-color: ", ";\n"], ["\n  display: block;\n  width: 100%;\n  height: 16px;\n  color: inherit;\n  outline: none;\n  background-color: ", ";\n"])), function (p) { return COLORS[p.index]; });
var renderBodyCellWithData = function (parentProps) {
    return function (column, dataRow) { return renderBodyCell(parentProps, column, dataRow); };
};
function TagValue(props) {
    var value = props.value;
    return <div>{value.name}</div>;
}
var _TagExplorer = /** @class */ (function (_super) {
    __extends(_TagExplorer, _super);
    function _TagExplorer() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.state = {
            tagOrder: HEADER_OPTIONS[0].value,
            aggregateColumn: DURATION_OPTIONS[0].value,
        };
        return _this;
    }
    _TagExplorer.prototype.setTagOrder = function (value) {
        this.setState({
            tagOrder: value,
        });
    };
    _TagExplorer.prototype.setAggregateColumn = function (value) {
        this.setState({
            aggregateColumn: value,
        });
    };
    _TagExplorer.prototype.render = function () {
        var _this = this;
        var _a = this.props, eventView = _a.eventView, organization = _a.organization, location = _a.location;
        var _b = this.state, tagOrder = _b.tagOrder, aggregateColumn = _b.aggregateColumn;
        var handleCursor = function () { };
        var sortDropdownOptions = HEADER_OPTIONS;
        var columnDropdownOptions = DURATION_OPTIONS;
        var selectedSort = sortDropdownOptions.find(function (o) { return o.value === tagOrder; }) || sortDropdownOptions[0];
        var selectedColumn = columnDropdownOptions.find(function (o) { return o.value === aggregateColumn; }) ||
            columnDropdownOptions[0];
        return (<SegmentExplorerQuery eventView={eventView} orgSlug={organization.slug} location={location} tagOrder={tagOrder} aggregateColumn={aggregateColumn} limit={5}>
        {function (_a) {
                var isLoading = _a.isLoading, tableData = _a.tableData, pageLinks = _a.pageLinks;
                return (<React.Fragment>
              <TagsHeader selectedSort={selectedSort} sortOptions={sortDropdownOptions} selectedColumn={selectedColumn} columnOptions={columnDropdownOptions} handleSortDropdownChange={function (v) { return _this.setTagOrder(v); }} handleColumnDropdownChange={function (v) { return _this.setAggregateColumn(v); }}/>
              <GridEditable isLoading={isLoading} data={tableData ? tableData : []} columnOrder={COLUMN_ORDER} columnSortBy={[]} grid={{
                        renderBodyCell: renderBodyCellWithData(_this.props),
                    }} location={location}/>
              <StyledPagination pageLinks={pageLinks} onCursor={handleCursor} size="small"/>
            </React.Fragment>);
            }}
      </SegmentExplorerQuery>);
    };
    return _TagExplorer;
}(React.Component));
function TagsHeader(props) {
    var selectedSort = props.selectedSort, sortOptions = props.sortOptions, selectedColumn = props.selectedColumn, columnOptions = props.columnOptions, handleSortDropdownChange = props.handleSortDropdownChange, handleColumnDropdownChange = props.handleColumnDropdownChange;
    return (<Header>
      <DropdownControl data-test-id="sort-tag-values" button={function (_a) {
            var isOpen = _a.isOpen, getActorProps = _a.getActorProps;
            return (<StyledDropdownButton {...getActorProps()} isOpen={isOpen} prefix={t('Sort')} size="small">
            {selectedSort.label}
          </StyledDropdownButton>);
        }}>
        {sortOptions.map(function (_a) {
            var value = _a.value, label = _a.label;
            return (<DropdownItem data-test-id={"option-" + value} key={value} onSelect={handleSortDropdownChange} eventKey={value} isActive={value === selectedSort.value}>
            {label}
          </DropdownItem>);
        })}
      </DropdownControl>
      <DropdownControl data-test-id="tag-column-performance" button={function (_a) {
            var isOpen = _a.isOpen, getActorProps = _a.getActorProps;
            return (<StyledDropdownButton {...getActorProps()} isOpen={isOpen} prefix={t('Column')} size="small">
            {selectedColumn.label}
          </StyledDropdownButton>);
        }}>
        {columnOptions.map(function (_a) {
            var value = _a.value, label = _a.label;
            return (<DropdownItem data-test-id={"option-" + value} key={value} onSelect={handleColumnDropdownChange} eventKey={value} isActive={value === selectedColumn.value}>
            {label}
          </DropdownItem>);
        })}
      </DropdownControl>
    </Header>);
}
var Header = styled('div')(templateObject_4 || (templateObject_4 = __makeTemplateObject(["\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  margin: 0 0 ", " 0;\n"], ["\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  margin: 0 0 ", " 0;\n"])), space(1));
var StyledDropdownButton = styled(DropdownButton)(templateObject_5 || (templateObject_5 = __makeTemplateObject(["\n  min-width: 145px;\n"], ["\n  min-width: 145px;\n"])));
var StyledPagination = styled(Pagination)(templateObject_6 || (templateObject_6 = __makeTemplateObject(["\n  margin: 0 0 ", " 0;\n"], ["\n  margin: 0 0 ", " 0;\n"])), space(3));
export var TagExplorer = _TagExplorer;
var templateObject_1, templateObject_2, templateObject_3, templateObject_4, templateObject_5, templateObject_6;
//# sourceMappingURL=tagExplorer.jsx.map