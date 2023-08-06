import { __assign, __makeTemplateObject } from "tslib";
import React from 'react';
import styled from '@emotion/styled';
import Button from 'app/components/button';
import SearchBar from 'app/components/events/searchBar';
import { IconAdd, IconDelete } from 'app/icons';
import { t } from 'app/locale';
import space from 'app/styles/space';
import Field from 'app/views/settings/components/forms/field';
import SelectField from 'app/views/settings/components/forms/selectField';
function Queries(_a) {
    var _b, _c;
    var organization = _a.organization, projectId = _a.projectId, metrics = _a.metrics, queries = _a.queries, onRemoveQuery = _a.onRemoveQuery, onAddQuery = _a.onAddQuery, onChangeQuery = _a.onChangeQuery, metric = _a.metric;
    function handleFieldChange(queryIndex, field) {
        var widgetQuery = queries[queryIndex];
        return function handleChange(value) {
            var _a;
            var newQuery = __assign(__assign({}, widgetQuery), (_a = {}, _a[field] = value, _a));
            onChangeQuery(queryIndex, newQuery);
        };
    }
    var aggregations = metric
        ? (_c = (_b = metrics.find(function (m) { return m.name === metric.name; })) === null || _b === void 0 ? void 0 : _b.operations) !== null && _c !== void 0 ? _c : []
        : [];
    return (<div>
      {queries.map(function (query, queryIndex) {
            var _a;
            return (<StyledField key={queryIndex} inline={false} flexibleControlStateSize stacked>
            <Fields displayDeleteButton={queries.length > 1}>
              <SearchBar placeholder={t('Search for tag')} organization={organization} projectIds={[Number(projectId)]} query={query.tags} fields={[]} onChange={function (value) { return handleFieldChange(queryIndex, 'tags')(value); }} onBlur={function (value) { return handleFieldChange(queryIndex, 'tags')(value); }} useFormWrapper={false}/>
              <StyledSelectField name="groupBy" placeholder={t('Select Group By')} choices={((_a = metric === null || metric === void 0 ? void 0 : metric.tags) !== null && _a !== void 0 ? _a : []).map(function (tag) { return [tag, tag]; })} value={query.groupBy} onChange={function (value) {
                    return handleFieldChange(queryIndex, 'groupBy')(value);
                }} inline={false} allowClear={false} flexibleControlStateSize stacked/>
              <StyledSelectField name="aggregation" placeholder={t('Select Aggregation')} choices={aggregations.map(function (aggregation) { return [aggregation, aggregation]; })} value={query.aggregation} onChange={function (value) { return handleFieldChange(queryIndex, 'aggregation')(value); }} inline={false} allowClear={false} flexibleControlStateSize stacked/>
              {queries.length > 1 && (<Button size="zero" borderless onClick={function (event) {
                        event.preventDefault();
                        onRemoveQuery(queryIndex);
                    }} icon={<IconDelete />} title={t('Remove query')} label={t('Remove query')}/>)}
            </Fields>
          </StyledField>);
        })}
      <Button size="small" icon={<IconAdd isCircled/>} onClick={function (event) {
            event.preventDefault();
            onAddQuery();
        }}>
        {t('Add Query')}
      </Button>
    </div>);
}
export default Queries;
var Fields = styled('div')(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  display: grid;\n  grid-template-columns: ", ";\n  grid-gap: ", ";\n  align-items: center;\n"], ["\n  display: grid;\n  grid-template-columns: ",
    ";\n  grid-gap: ", ";\n  align-items: center;\n"])), function (p) {
    return p.displayDeleteButton ? '1fr 0.5fr 0.5fr max-content' : '1fr 0.5fr 0.5fr';
}, space(1));
var StyledField = styled(Field)(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  padding-right: 0;\n"], ["\n  padding-right: 0;\n"])));
var StyledSelectField = styled(SelectField)(templateObject_3 || (templateObject_3 = __makeTemplateObject(["\n  padding-right: 0;\n  padding-bottom: 0;\n"], ["\n  padding-right: 0;\n  padding-bottom: 0;\n"])));
var templateObject_1, templateObject_2, templateObject_3;
//# sourceMappingURL=queries.jsx.map