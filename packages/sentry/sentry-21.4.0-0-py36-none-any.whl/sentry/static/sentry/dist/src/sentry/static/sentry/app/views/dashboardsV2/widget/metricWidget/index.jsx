import { __assign, __awaiter, __extends, __generator, __makeTemplateObject, __rest } from "tslib";
import React from 'react';
import { components } from 'react-select';
import styled from '@emotion/styled';
import cloneDeep from 'lodash/cloneDeep';
import set from 'lodash/set';
import Highlight from 'app/components/highlight';
import * as Layout from 'app/components/layouts/thirds';
import GlobalSelectionHeader from 'app/components/organizations/globalSelectionHeader';
import PickProjectToContinue from 'app/components/pickProjectToContinue';
import { t } from 'app/locale';
import { PageContent } from 'app/styles/organization';
import withGlobalSelection from 'app/utils/withGlobalSelection';
import withProjects from 'app/utils/withProjects';
import AsyncView from 'app/views/asyncView';
import SelectField from 'app/views/settings/components/forms/selectField';
import BuildStep from '../buildStep';
import BuildSteps from '../buildSteps';
import ChooseDataSetStep from '../choseDataStep';
import Header from '../header';
import { DataSet } from '../utils';
import Card from './card';
import Queries from './queries';
var newQuery = {
    tags: '',
    groupBy: '',
    aggregation: '',
};
var MetricWidget = /** @class */ (function (_super) {
    __extends(MetricWidget, _super);
    function MetricWidget() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.handleTitleChange = function (title) {
            _this.setState({ title: title });
        };
        _this.handleMetricChange = function (metric) {
            _this.setState({ metric: metric, queries: [__assign({}, newQuery)] });
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
        _this.handleProjectChange = function (selectedProjects) {
            var _a = _this.props, projects = _a.projects, router = _a.router, location = _a.location, organization = _a.organization;
            var newlySelectedProject = projects.find(function (p) { return p.id === String(selectedProjects[0]); });
            // if we change project in global header, we need to sync the project slug in the URL
            if (newlySelectedProject === null || newlySelectedProject === void 0 ? void 0 : newlySelectedProject.id) {
                router.replace({
                    pathname: "/organizations/" + organization.slug + "/dashboards/widget/new/",
                    query: __assign(__assign({}, location.query), { project: newlySelectedProject.id, environment: undefined }),
                });
            }
        };
        return _this;
    }
    MetricWidget.prototype.getDefaultState = function () {
        return __assign(__assign({}, _super.prototype.getDefaultState.call(this)), { title: t('Custom Widget'), metrics: [], queries: [__assign({}, newQuery)] });
    };
    MetricWidget.prototype.componentDidMount = function () {
        this.fetchMetrics();
    };
    MetricWidget.prototype.componentDidUpdate = function (prevProps, prevState) {
        if (!this.isProjectMissingInUrl() && !this.state.metrics.length) {
            this.fetchMetrics();
        }
        _super.prototype.componentDidUpdate.call(this, prevProps, prevState);
    };
    MetricWidget.prototype.fetchMetrics = function () {
        return __awaiter(this, void 0, void 0, function () {
            var newMetrics, error_1;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0:
                        if (this.isProjectMissingInUrl() || !!this.state.metrics.length) {
                            return [2 /*return*/];
                        }
                        _a.label = 1;
                    case 1:
                        _a.trys.push([1, 3, , 4]);
                        return [4 /*yield*/, Promise.resolve([
                                {
                                    name: 'session',
                                    type: 'counter',
                                    operations: ['sum'],
                                    tags: ['session.status', 'project', 'release'],
                                    unit: null,
                                },
                                {
                                    name: 'user',
                                    type: 'set',
                                    operations: ['count_unique'],
                                    tags: ['session.status', 'project', 'release'],
                                    unit: null,
                                },
                                {
                                    name: 'session.duration',
                                    type: 'distribution',
                                    operations: ['avg', 'p50', 'p75', 'p90', 'p95', 'p99', 'max'],
                                    tags: ['session.status', 'project', 'release'],
                                    unit: 'seconds',
                                },
                            ])];
                    case 2:
                        newMetrics = _a.sent();
                        this.setState({ metrics: newMetrics });
                        return [3 /*break*/, 4];
                    case 3:
                        error_1 = _a.sent();
                        this.setState({ error: error_1 });
                        return [3 /*break*/, 4];
                    case 4: return [2 /*return*/];
                }
            });
        });
    };
    MetricWidget.prototype.isProjectMissingInUrl = function () {
        var projectId = this.props.location.query.project;
        return !projectId || typeof projectId !== 'string';
    };
    MetricWidget.prototype.renderBody = function () {
        var _a = this.props, organization = _a.organization, router = _a.router, projects = _a.projects, onChangeDataSet = _a.onChangeDataSet, selection = _a.selection, location = _a.location, loadingProjects = _a.loadingProjects;
        var _b = this.state, title = _b.title, metrics = _b.metrics, metric = _b.metric, queries = _b.queries;
        var query = location.query;
        var projectId = query.project;
        var orgSlug = organization.slug;
        if (loadingProjects) {
            return this.renderLoading();
        }
        var selectedProject = projects.find(function (project) { return project.id === projectId; });
        if (this.isProjectMissingInUrl() || !selectedProject) {
            return (<PickProjectToContinue router={router} projects={projects.map(function (project) { return ({ id: project.id, slug: project.slug }); })} nextPath={"/organizations/" + orgSlug + "/dashboards/widget/new/?dataSet=metrics"} noProjectRedirectPath={"/organizations/" + orgSlug + "/dashboards/"}/>);
        }
        return (<GlobalSelectionHeader onUpdateProjects={this.handleProjectChange} disableMultipleProjectSelection skipLoadLastUsed>
        <StyledPageContent>
          <Header orgSlug={orgSlug} title={title} onChangeTitle={this.handleTitleChange}/>
          <Layout.Body>
            <BuildSteps>
              <Card router={router} location={location} selection={selection} organization={organization} api={this.api} project={selectedProject} widget={{
                title: title,
                queries: queries,
                yAxis: metric === null || metric === void 0 ? void 0 : metric.name,
            }}/>
              <ChooseDataSetStep value={DataSet.METRICS} onChange={onChangeDataSet}/>
              <BuildStep title={t('Choose your y-axis metric')} description={t('Determine what type of metric you want to graph by.')}>
                <StyledSelectField name="metric" choices={metrics.map(function (m) { return [m, m.name]; })} placeholder={t('Select metric')} onChange={this.handleMetricChange} components={{
                Option: function (_a) {
                    var label = _a.label, optionProps = __rest(_a, ["label"]);
                    var selectProps = optionProps.selectProps;
                    var inputValue = selectProps.inputValue;
                    return (<components.Option label={label} {...optionProps}>
                          <Highlight text={inputValue !== null && inputValue !== void 0 ? inputValue : ''}>{label}</Highlight>
                        </components.Option>);
                },
            }} inline={false} flexibleControlStateSize stacked allowClear/>
              </BuildStep>
              <BuildStep title={t('Begin your search')} description={t('Add another query to compare projects, tags, etc.')}>
                <Queries organization={organization} projectId={selectedProject.id} metrics={metrics} metric={metric} queries={queries} onAddQuery={this.handleAddQuery} onRemoveQuery={this.handleRemoveQuery} onChangeQuery={this.handleChangeQuery}/>
              </BuildStep>
            </BuildSteps>
          </Layout.Body>
        </StyledPageContent>
      </GlobalSelectionHeader>);
    };
    return MetricWidget;
}(AsyncView));
export default withProjects(withGlobalSelection(MetricWidget));
var StyledPageContent = styled(PageContent)(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  padding: 0;\n"], ["\n  padding: 0;\n"])));
var StyledSelectField = styled(SelectField)(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  padding-right: 0;\n"], ["\n  padding-right: 0;\n"])));
var templateObject_1, templateObject_2;
//# sourceMappingURL=index.jsx.map