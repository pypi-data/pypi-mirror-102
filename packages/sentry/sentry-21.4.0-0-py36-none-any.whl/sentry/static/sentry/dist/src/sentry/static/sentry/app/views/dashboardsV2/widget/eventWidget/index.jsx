import { __assign, __extends, __makeTemplateObject } from "tslib";
import React from 'react';
import styled from '@emotion/styled';
import cloneDeep from 'lodash/cloneDeep';
import set from 'lodash/set';
import WidgetQueryFields from 'app/components/dashboards/widgetQueryFields';
import SelectControl from 'app/components/forms/selectControl';
import * as Layout from 'app/components/layouts/thirds';
import GlobalSelectionHeader from 'app/components/organizations/globalSelectionHeader';
import { PanelAlert } from 'app/components/panels';
import { t } from 'app/locale';
import { PageContent } from 'app/styles/organization';
import space from 'app/styles/space';
import Measurements from 'app/utils/measurements/measurements';
import withGlobalSelection from 'app/utils/withGlobalSelection';
import withOrganization from 'app/utils/withOrganization';
import withTags from 'app/utils/withTags';
import AsyncView from 'app/views/asyncView';
import { DisplayType } from 'app/views/dashboardsV2/types';
import WidgetCard from 'app/views/dashboardsV2/widgetCard';
import { generateFieldOptions } from 'app/views/eventsV2/utils';
import { DEFAULT_STATS_PERIOD } from '../../data';
import BuildStep from '../buildStep';
import BuildSteps from '../buildSteps';
import ChooseDataSetStep from '../choseDataStep';
import Header from '../header';
import { DataSet, displayTypes } from '../utils';
import Queries from './queries';
var newQuery = {
    name: '',
    fields: ['count()'],
    conditions: '',
    orderby: '',
};
var EventWidget = /** @class */ (function (_super) {
    __extends(EventWidget, _super);
    function EventWidget() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.handleFieldChange = function (field, value) {
            _this.setState(function (state) {
                var _a;
                return (__assign(__assign({}, state), (_a = {}, _a[field] = value, _a)));
            });
        };
        _this.handleRemoveQuery = function (index) {
            _this.setState(function (state) {
                var newState = cloneDeep(state);
                newState.queries.splice(index, index + 1);
                return newState;
            });
        };
        _this.handleAddQuery = function () {
            _this.setState(function (state) {
                var newState = cloneDeep(state);
                newState.queries.push(cloneDeep(newQuery));
                return newState;
            });
        };
        _this.handleChangeQuery = function (index, query) {
            _this.setState(function (state) {
                var newState = cloneDeep(state);
                set(newState, "queries." + index, query);
                return newState;
            });
        };
        return _this;
    }
    EventWidget.prototype.getDefaultState = function () {
        return __assign(__assign({}, _super.prototype.getDefaultState.call(this)), { title: t('Custom %s Widget', DisplayType.AREA), displayType: DisplayType.AREA, interval: '5m', queries: [__assign({}, newQuery)] });
    };
    EventWidget.prototype.renderBody = function () {
        var _this = this;
        var _a = this.props, organization = _a.organization, onChangeDataSet = _a.onChangeDataSet, selection = _a.selection, tags = _a.tags;
        var _b = this.state, title = _b.title, displayType = _b.displayType, queries = _b.queries, interval = _b.interval;
        var orgSlug = organization.slug;
        function fieldOptions(measurementKeys) {
            return generateFieldOptions({
                organization: organization,
                tagKeys: Object.values(tags).map(function (_a) {
                    var key = _a.key;
                    return key;
                }),
                measurementKeys: measurementKeys,
            });
        }
        return (<GlobalSelectionHeader skipLoadLastUsed={organization.features.includes('global-views')} defaultSelection={{
                datetime: {
                    start: null,
                    end: null,
                    utc: false,
                    period: DEFAULT_STATS_PERIOD,
                },
            }}>
        <StyledPageContent>
          <Header orgSlug={orgSlug} title={title} onChangeTitle={function (newTitle) { return _this.handleFieldChange('title', newTitle); }}/>
          <Layout.Body>
            <BuildSteps>
              <BuildStep title={t('Choose your visualization')} description={t('This is a preview of how your widget will appear in the dashboard.')}>
                <VisualizationWrapper>
                  <SelectControl name="displayType" options={Object.keys(displayTypes).map(function (value) { return ({
                label: displayTypes[value],
                value: value,
            }); })} value={displayType} onChange={function (option) {
                _this.handleFieldChange('displayType', option.value);
            }}/>
                  <WidgetCard api={this.api} organization={organization} selection={selection} widget={{ title: title, queries: queries, displayType: displayType, interval: interval }} isEditing={false} onDelete={function () { return undefined; }} onEdit={function () { return undefined; }} renderErrorMessage={function (errorMessage) {
                return typeof errorMessage === 'string' && (<PanelAlert type="error">{errorMessage}</PanelAlert>);
            }} isSorting={false} currentWidgetDragging={false}/>
                </VisualizationWrapper>
              </BuildStep>
              <ChooseDataSetStep value={DataSet.EVENTS} onChange={onChangeDataSet}/>
              <BuildStep title={t('Begin your search')} description={t('Add another query to compare projects, tags, etc.')}>
                <Queries queries={queries} selectedProjectIds={selection.projects} organization={organization} displayType={displayType} onRemoveQuery={this.handleRemoveQuery} onAddQuery={this.handleAddQuery} onChangeQuery={this.handleChangeQuery}/>
              </BuildStep>
              <Measurements>
                {function (_a) {
                var measurements = _a.measurements;
                var measurementKeys = Object.values(measurements).map(function (_a) {
                    var key = _a.key;
                    return key;
                });
                var amendedFieldOptions = fieldOptions(measurementKeys);
                var buildStepContent = (<WidgetQueryFields style={{ padding: 0 }} displayType={displayType} fieldOptions={amendedFieldOptions} fields={queries[0].fields} onChange={function (fields) {
                        queries.forEach(function (query, queryIndex) {
                            var clonedQuery = cloneDeep(query);
                            clonedQuery.fields = fields;
                            _this.handleChangeQuery(queryIndex, clonedQuery);
                        });
                    }}/>);
                return (<BuildStep title={displayType === DisplayType.TABLE
                        ? t('Choose your columns')
                        : t('Choose your y-axis')} description={t('We’ll use this to determine what gets graphed in the y-axis and any additional overlays.')}>
                      {buildStepContent}
                    </BuildStep>);
            }}
              </Measurements>
            </BuildSteps>
          </Layout.Body>
        </StyledPageContent>
      </GlobalSelectionHeader>);
    };
    return EventWidget;
}(AsyncView));
export default withOrganization(withGlobalSelection(withTags(EventWidget)));
var StyledPageContent = styled(PageContent)(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  padding: 0;\n"], ["\n  padding: 0;\n"])));
var VisualizationWrapper = styled('div')(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  display: grid;\n  grid-gap: ", ";\n"], ["\n  display: grid;\n  grid-gap: ", ";\n"])), space(1.5));
var templateObject_1, templateObject_2;
//# sourceMappingURL=index.jsx.map