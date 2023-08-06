import { __assign, __read } from "tslib";
import React, { useEffect, useState } from 'react';
import Alert from 'app/components/alert';
import { IconWarning } from 'app/icons';
import { t } from 'app/locale';
import { PageContent } from 'app/styles/organization';
import EventWidget from '../eventWidget';
import MetricWidget from '../metricWidget';
import { DataSet } from '../utils';
function WidgetNew(props) {
    var _a = __read(useState(DataSet.EVENTS), 2), dataSet = _a[0], setDataSet = _a[1];
    useEffect(function () {
        checkDataSet();
    });
    function checkDataSet() {
        var params = props.params, location = props.location, router = props.router;
        var orgSlug = params.orgId;
        var query = location.query;
        var queryDataSet = query === null || query === void 0 ? void 0 : query.dataSet;
        if (!queryDataSet) {
            router.replace({
                pathname: "/organizations/" + orgSlug + "/dashboards/widget/new/",
                query: __assign(__assign({}, location.query), { dataSet: DataSet.EVENTS }),
            });
            return;
        }
        if (queryDataSet !== DataSet.EVENTS && queryDataSet !== DataSet.METRICS) {
            setDataSet(undefined);
            return;
        }
        if (queryDataSet === DataSet.METRICS) {
            if (dataSet === DataSet.METRICS) {
                return;
            }
            setDataSet(DataSet.METRICS);
            return;
        }
        if (dataSet === DataSet.EVENTS) {
            return;
        }
        setDataSet(DataSet.EVENTS);
    }
    function handleDataSetChange(newDataSet) {
        var params = props.params, location = props.location, router = props.router;
        var orgSlug = params.orgId;
        router.replace({
            pathname: "/organizations/" + orgSlug + "/dashboards/widget/new/",
            query: __assign(__assign({}, location.query), { dataSet: newDataSet }),
        });
    }
    if (!dataSet) {
        return (<PageContent>
        <Alert type="error" icon={<IconWarning />}>
          {t('Data set not found.')}
        </Alert>
      </PageContent>);
    }
    if (dataSet === DataSet.EVENTS) {
        return <EventWidget onChangeDataSet={handleDataSetChange}/>;
    }
    return <MetricWidget {...props} onChangeDataSet={handleDataSetChange}/>;
}
export default WidgetNew;
//# sourceMappingURL=widgetNew.jsx.map