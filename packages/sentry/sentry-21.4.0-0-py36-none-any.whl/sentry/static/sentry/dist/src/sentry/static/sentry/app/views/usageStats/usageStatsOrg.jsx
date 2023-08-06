import { __assign, __extends, __makeTemplateObject } from "tslib";
import React from 'react';
import styled from '@emotion/styled';
import * as Sentry from '@sentry/react';
import moment from 'moment';
import AsyncComponent from 'app/components/asyncComponent';
import Card from 'app/components/card';
import ErrorPanel from 'app/components/charts/errorPanel';
import OptionSelector from 'app/components/charts/optionSelector';
import { ChartControls, HeaderTitle, InlineContainer, SectionValue, } from 'app/components/charts/styles';
import LoadingIndicator from 'app/components/loadingIndicator';
import { Panel, PanelBody } from 'app/components/panels';
import QuestionTooltip from 'app/components/questionTooltip';
import TextOverflow from 'app/components/textOverflow';
import { IconCalendar, IconWarning } from 'app/icons';
import { t, tct } from 'app/locale';
import space from 'app/styles/space';
import { DataCategory } from 'app/types';
import { Outcome } from './types';
import UsageChart, { CHART_OPTIONS_DATA_TRANSFORM, CHART_OPTIONS_DATACATEGORY, ChartDataTransform, } from './usageChart';
import { formatUsageWithUnits } from './utils';
var UsageStatsOrganization = /** @class */ (function (_super) {
    __extends(UsageStatsOrganization, _super);
    function UsageStatsOrganization() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.renderChartFooter = function () {
            var _a = _this.props, dataCategory = _a.dataCategory, onChangeDataCategory = _a.onChangeDataCategory;
            var chartDataTransform = _this.state.chartDataTransform;
            return (<ChartControls>
        <InlineContainer>
          <SectionValue>
            <IconCalendar />
          </SectionValue>
          <SectionValue>
            {/*
                TODO(org-stats): Add calendar dropdown for user to select date range
    
                {moment(usagePeriodStart).format('ll')}
                {' — '}
                {moment(usagePeriodEnd).format('ll')}
                */}
          </SectionValue>
        </InlineContainer>
        <InlineContainer>
          <OptionSelector title={t('Display')} menuWidth="135px" selected={dataCategory} options={CHART_OPTIONS_DATACATEGORY} onChange={function (val) { return onChangeDataCategory(val); }}/>
          <OptionSelector title={t('Type')} selected={chartDataTransform} options={CHART_OPTIONS_DATA_TRANSFORM} onChange={function (val) {
                    return _this.handleSelectDataTransform(val);
                }}/>
        </InlineContainer>
      </ChartControls>);
        };
        return _this;
    }
    UsageStatsOrganization.prototype.getDefaultState = function () {
        return __assign(__assign({}, _super.prototype.getDefaultState.call(this)), { chartDataTransform: ChartDataTransform.CUMULATIVE });
    };
    UsageStatsOrganization.prototype.getEndpoints = function () {
        return [['orgStats', this.endpointPath, { query: this.endpointQuery }]];
    };
    Object.defineProperty(UsageStatsOrganization.prototype, "endpointPath", {
        get: function () {
            var organization = this.props.organization;
            return "/organizations/" + organization.slug + "/stats_v2/";
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(UsageStatsOrganization.prototype, "endpointQuery", {
        get: function () {
            var _a = this.props, dateStart = _a.dateStart, dateEnd = _a.dateEnd;
            return {
                statsPeriod: dateEnd.diff(dateStart, 'd') + "d",
                interval: '1d',
                groupBy: ['category', 'outcome'],
                field: ['sum(quantity)'],
            };
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(UsageStatsOrganization.prototype, "chartMetadata", {
        get: function () {
            var orgStats = this.state.orgStats;
            return __assign({}, this.mapSeriesToChart(orgStats));
        },
        enumerable: false,
        configurable: true
    });
    UsageStatsOrganization.prototype.handleSelectDataTransform = function (value) {
        this.setState({ chartDataTransform: value });
    };
    UsageStatsOrganization.prototype.mapSeriesToChart = function (orgStats) {
        var _this = this;
        var cardData = {
            total: '-',
            accepted: '-',
            dropped: '-',
            filtered: '-',
        };
        var chartData = {
            accepted: [],
            dropped: [],
            projected: [],
        };
        if (!orgStats) {
            return { cardData: cardData, chartData: chartData };
        }
        try {
            var dataCategory_1 = this.props.dataCategory;
            var rollup = '1d'; // TODO(org-stats)
            var dateTimeFormat_1 = rollup === '1d' ? 'MMM D' : 'MMM D, HH:mm';
            var usageStats_1 = orgStats.intervals.map(function (interval) {
                var dateTime = moment(interval);
                return {
                    date: dateTime.format(dateTimeFormat_1),
                    total: 0,
                    accepted: 0,
                    filtered: 0,
                    dropped: { total: 0 },
                };
            });
            // Tally totals for card data
            var count_1 = {
                total: 0,
                accepted: 0,
                dropped: 0,
                invalid: 0,
                filtered: 0,
            };
            orgStats.groups.forEach(function (group) {
                var _a = group.by, outcome = _a.outcome, category = _a.category;
                // HACK The backend enum are singular, but the frontend enums are plural
                if (!dataCategory_1.includes("" + category)) {
                    return;
                }
                count_1.total += group.totals['sum(quantity)'];
                count_1[outcome] += group.totals['sum(quantity)'];
                group.series['sum(quantity)'].forEach(function (stat, i) {
                    if (outcome === Outcome.DROPPED || outcome === Outcome.INVALID) {
                        usageStats_1[i].dropped.total += stat;
                    }
                    usageStats_1[i][outcome] += stat;
                });
            });
            // Invalid data is dropped
            count_1.dropped += count_1.invalid;
            delete count_1.invalid;
            usageStats_1.forEach(function (stat) {
                stat.total = stat.accepted + stat.filtered + stat.dropped.total;
                // Chart Data
                chartData.accepted.push({ value: [stat.date, stat.accepted] });
                chartData.dropped.push({ value: [stat.date, stat.dropped.total] });
            });
            var formatOptions = {
                isAbbreviated: dataCategory_1 !== DataCategory.ATTACHMENTS,
                useUnitScaling: dataCategory_1 === DataCategory.ATTACHMENTS,
            };
            return {
                cardData: {
                    total: formatUsageWithUnits(count_1.total, dataCategory_1, formatOptions),
                    accepted: formatUsageWithUnits(count_1.accepted, dataCategory_1, formatOptions),
                    dropped: formatUsageWithUnits(count_1.dropped, dataCategory_1, formatOptions),
                    filtered: formatUsageWithUnits(count_1.filtered, dataCategory_1, formatOptions),
                },
                chartData: chartData,
            };
        }
        catch (err) {
            Sentry.withScope(function (scope) {
                scope.setContext('query', _this.endpointQuery);
                scope.setContext('body', orgStats);
                Sentry.captureException(err);
            });
            return {
                cardData: cardData,
                chartData: chartData,
                error: err,
            };
        }
    };
    UsageStatsOrganization.prototype.renderCards = function () {
        var _a = this.props, dataCategory = _a.dataCategory, dataCategoryName = _a.dataCategoryName;
        var _b = this.chartMetadata.cardData, total = _b.total, accepted = _b.accepted, dropped = _b.dropped, filtered = _b.filtered;
        var cardMetadata = [
            {
                title: tct('Total [dataCategory]', { dataCategory: dataCategoryName }),
                value: total,
            },
            {
                title: t('Accepted'),
                value: accepted,
            },
            {
                title: t('Filtered'),
                description: tct('Filtered [dataCategory] were blocked due to your inbound data filter rules', { dataCategory: dataCategory }),
                value: filtered,
            },
            // TODO(org-stats): Need a better description for dropped data
            {
                title: t('Dropped'),
                description: tct('Dropped [dataCategory] were discarded due to rate-limits, quota limits, or spike protection', { dataCategory: dataCategory }),
                value: dropped,
            },
        ];
        return (<CardWrapper>
        {cardMetadata.map(function (c, i) { return (<StyledCard key={i}>
            <HeaderTitle>
              <TextOverflow>{c.title}</TextOverflow>
              {c.description && (<QuestionTooltip size="sm" position="top" title={c.description}/>)}
            </HeaderTitle>
            <CardContent>
              <TextOverflow>{c.value}</TextOverflow>
            </CardContent>
          </StyledCard>); })}
      </CardWrapper>);
    };
    UsageStatsOrganization.prototype.renderChart = function () {
        var _a = this.props, dateStart = _a.dateStart, dateEnd = _a.dateEnd, dataCategory = _a.dataCategory;
        var _b = this.state, chartDataTransform = _b.chartDataTransform, error = _b.error, loading = _b.loading, orgStats = _b.orgStats;
        if (loading) {
            return (<Panel>
          <PanelBody>
            <LoadingIndicator />
          </PanelBody>
        </Panel>);
        }
        var _c = this.chartMetadata, chartData = _c.chartData, chartError = _c.error;
        if (error || chartError || !orgStats) {
            return (<Panel>
          <PanelBody>
            <ErrorPanel height="256px">
              <IconWarning color="gray300" size="lg"/>
            </ErrorPanel>
          </PanelBody>
        </Panel>);
        }
        var usageDateStart = dateStart.format('YYYY-MM-DD');
        var usageDateEnd = dateEnd.format('YYYY-MM-DD');
        return (<UsageChart footer={this.renderChartFooter()} dataCategory={dataCategory} dataTransform={chartDataTransform} usageDateStart={usageDateStart} usageDateEnd={usageDateEnd} usageStats={chartData}/>);
    };
    UsageStatsOrganization.prototype.renderComponent = function () {
        return (<React.Fragment>
        {this.renderCards()}
        {this.renderChart()}
      </React.Fragment>);
    };
    return UsageStatsOrganization;
}(AsyncComponent));
export default UsageStatsOrganization;
var CardWrapper = styled('div')(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  display: grid;\n  grid-auto-flow: column;\n  grid-auto-columns: 1fr;\n  grid-auto-rows: 1fr;\n  grid-gap: ", ";\n  margin-bottom: ", ";\n\n  @media (max-width: ", ") {\n    grid-auto-flow: row;\n  }\n"], ["\n  display: grid;\n  grid-auto-flow: column;\n  grid-auto-columns: 1fr;\n  grid-auto-rows: 1fr;\n  grid-gap: ", ";\n  margin-bottom: ", ";\n\n  @media (max-width: ", ") {\n    grid-auto-flow: row;\n  }\n"])), space(2), space(3), function (p) { return p.theme.breakpoints[0]; });
var StyledCard = styled(Card)(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  align-items: flex-start;\n  min-height: 95px;\n  padding: ", " ", ";\n  color: ", ";\n"], ["\n  align-items: flex-start;\n  min-height: 95px;\n  padding: ", " ", ";\n  color: ", ";\n"])), space(2), space(3), function (p) { return p.theme.textColor; });
var CardContent = styled('div')(templateObject_3 || (templateObject_3 = __makeTemplateObject(["\n  margin-top: ", ";\n  font-size: 32px;\n"], ["\n  margin-top: ", ";\n  font-size: 32px;\n"])), space(1));
var templateObject_1, templateObject_2, templateObject_3;
//# sourceMappingURL=usageStatsOrg.jsx.map