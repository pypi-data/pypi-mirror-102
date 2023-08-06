import { __assign, __extends, __read, __spreadArray } from "tslib";
import React from 'react';
import { browserHistory } from 'react-router';
import DropdownLink from 'app/components/dropdownLink';
import ProjectBadge from 'app/components/idBadge/projectBadge';
import { generateMultiTransactionsTarget, generateSingleErrorTarget, generateSingleTransactionTarget, } from 'app/components/quickTrace/utils';
import Tooltip from 'app/components/tooltip';
import { backend, frontend } from 'app/data/platformCategories';
import { IconFire } from 'app/icons';
import { t, tct, tn } from 'app/locale';
import { trackAnalyticsEvent } from 'app/utils/analytics';
import { getDuration } from 'app/utils/formatters';
import localStorage from 'app/utils/localStorage';
import { parseQuickTrace } from 'app/utils/performance/quickTrace/utils';
import Projects from 'app/utils/projects';
var FRONTEND_PLATFORMS = __spreadArray([], __read(frontend));
var BACKEND_PLATFORMS = __spreadArray([], __read(backend));
import { DropdownItem, DropdownItemSubContainer, ErrorNodeContent, EventNode, ExternalDropdownLink, QuickTraceContainer, SectionSubtext, SingleEventHoverText, StyledTruncate, TraceConnector, } from './styles';
var TOOLTIP_PREFIX = {
    root: 'root',
    ancestors: 'ancestor',
    parent: 'parent',
    current: '',
    children: 'child',
    descendants: 'descendant',
};
export default function QuickTrace(_a) {
    var event = _a.event, quickTrace = _a.quickTrace, location = _a.location, organization = _a.organization, anchor = _a.anchor, errorDest = _a.errorDest, transactionDest = _a.transactionDest;
    var parsedQuickTrace;
    try {
        parsedQuickTrace = parseQuickTrace(quickTrace, event);
    }
    catch (error) {
        return <React.Fragment>{'\u2014'}</React.Fragment>;
    }
    var traceLength = quickTrace.trace && quickTrace.trace.length;
    var root = parsedQuickTrace.root, ancestors = parsedQuickTrace.ancestors, parent = parsedQuickTrace.parent, children = parsedQuickTrace.children, descendants = parsedQuickTrace.descendants, current = parsedQuickTrace.current;
    var nodes = [];
    if (root) {
        nodes.push(<EventNodeSelector key="root-node" location={location} organization={organization} events={[root]} text={t('Root')} anchor={anchor} nodeKey="root" errorDest={errorDest} transactionDest={transactionDest}/>);
        nodes.push(<TraceConnector key="root-connector"/>);
    }
    if (ancestors === null || ancestors === void 0 ? void 0 : ancestors.length) {
        nodes.push(<EventNodeSelector key="ancestors-node" location={location} organization={organization} events={ancestors} text={tn('%s Ancestor', '%s Ancestors', ancestors.length)} extrasTarget={generateMultiTransactionsTarget(event, ancestors, organization, 'Ancestor')} anchor={anchor} nodeKey="ancestors" errorDest={errorDest} transactionDest={transactionDest}/>);
        nodes.push(<TraceConnector key="ancestors-connector"/>);
    }
    if (parent) {
        nodes.push(<EventNodeSelector key="parent-node" location={location} organization={organization} events={[parent]} text={t('Parent')} anchor={anchor} nodeKey="parent" errorDest={errorDest} transactionDest={transactionDest}/>);
        nodes.push(<TraceConnector key="parent-connector"/>);
    }
    var currentNode = (<EventNodeSelector key="current-node" location={location} organization={organization} text={t('This Event')} events={[current]} currentEvent={event} anchor={anchor} nodeKey="current" errorDest={errorDest} transactionDest={transactionDest}/>);
    if (traceLength === 1) {
        nodes.push(<Projects key="missing-services" orgId={organization.slug} slugs={[current.project_slug]}>
        {function (_a) {
                var projects = _a.projects;
                var project = projects.find(function (p) { return p.slug === current.project_slug; });
                if (project === null || project === void 0 ? void 0 : project.platform) {
                    if (BACKEND_PLATFORMS.includes(project.platform)) {
                        return (<React.Fragment>
                  <MissingServiceNode anchor={anchor} organization={organization} platform={project.platform} connectorSide="right"/>
                  {currentNode}
                </React.Fragment>);
                    }
                    else if (FRONTEND_PLATFORMS.includes(project.platform)) {
                        return (<React.Fragment>
                  {currentNode}
                  <MissingServiceNode anchor={anchor} organization={organization} platform={project.platform} connectorSide="left"/>
                </React.Fragment>);
                    }
                }
                return currentNode;
            }}
      </Projects>);
    }
    else {
        nodes.push(currentNode);
    }
    if (children.length) {
        nodes.push(<TraceConnector key="children-connector"/>);
        nodes.push(<EventNodeSelector key="children-node" location={location} organization={organization} events={children} text={tn('%s Child', '%s Children', children.length)} extrasTarget={generateMultiTransactionsTarget(event, children, organization, 'Children')} anchor={anchor} nodeKey="children" errorDest={errorDest} transactionDest={transactionDest}/>);
    }
    if (descendants === null || descendants === void 0 ? void 0 : descendants.length) {
        nodes.push(<TraceConnector key="descendants-connector"/>);
        nodes.push(<EventNodeSelector key="descendants-node" location={location} organization={organization} events={descendants} text={tn('%s Descendant', '%s Descendants', descendants.length)} extrasTarget={generateMultiTransactionsTarget(event, descendants, organization, 'Descendant')} anchor={anchor} nodeKey="descendants" errorDest={errorDest} transactionDest={transactionDest}/>);
    }
    return <QuickTraceContainer>{nodes}</QuickTraceContainer>;
}
function handleNode(key, organization) {
    trackAnalyticsEvent({
        eventKey: 'quick_trace.node.clicked',
        eventName: 'Quick Trace: Node clicked',
        organization_id: parseInt(organization.id, 10),
        node_key: key,
    });
}
function handleDropdownItem(target, key, organization, extra) {
    trackAnalyticsEvent({
        eventKey: 'quick_trace.dropdown.clicked' + (extra ? '_extra' : ''),
        eventName: 'Quick Trace: Dropdown clicked',
        organization_id: parseInt(organization.id, 10),
        node_key: key,
    });
    browserHistory.push(target);
}
function EventNodeSelector(_a) {
    var location = _a.location, organization = _a.organization, _b = _a.events, events = _b === void 0 ? [] : _b, text = _a.text, currentEvent = _a.currentEvent, extrasTarget = _a.extrasTarget, nodeKey = _a.nodeKey, anchor = _a.anchor, errorDest = _a.errorDest, transactionDest = _a.transactionDest, _c = _a.numEvents, numEvents = _c === void 0 ? 5 : _c;
    var errors = [];
    events.forEach(function (e) {
        var _a;
        (_a = e === null || e === void 0 ? void 0 : e.errors) === null || _a === void 0 ? void 0 : _a.forEach(function (error) {
            if (!currentEvent || currentEvent.id !== error.event_id) {
                errors.push(__assign(__assign({}, error), { transaction: e.transaction }));
            }
        });
    });
    // Filter out the current event so its not in the dropdown
    events = currentEvent ? events.filter(function (e) { return e.event_id !== currentEvent.id; }) : events;
    var type = nodeKey === 'current' ? 'black' : 'white';
    if (errors.length > 0 || (currentEvent && (currentEvent === null || currentEvent === void 0 ? void 0 : currentEvent.type) !== 'transaction')) {
        type = nodeKey === 'current' ? 'error' : 'warning';
        text = (<ErrorNodeContent>
        <IconFire size="xs"/>
        {text}
      </ErrorNodeContent>);
    }
    if (events.length + errors.length === 0) {
        return <EventNode type={type}>{text}</EventNode>;
    }
    else if (events.length + errors.length === 1) {
        /**
         * When there is only 1 event, clicking the node should take the user directly to
         * the event without additional steps.
         */
        var hoverText = errors.length ? (t('View the error for this Transaction')) : (<SingleEventHoverText event={events[0]}/>);
        var target = errors.length
            ? generateSingleErrorTarget(errors[0], organization, location, errorDest)
            : generateSingleTransactionTarget(events[0], organization, location, transactionDest);
        return (<StyledEventNode text={text} hoverText={hoverText} to={target} onClick={function () { return handleNode(nodeKey, organization); }} type={type}/>);
    }
    else {
        /**
         * When there is more than 1 event, clicking the node should expand a dropdown to
         * allow the user to select which event to go to.
         */
        var hoverText = tct('View [eventPrefix] [eventType]', {
            eventPrefix: TOOLTIP_PREFIX[nodeKey],
            eventType: errors.length && events.length
                ? 'events'
                : events.length
                    ? 'transactions'
                    : 'errors',
        });
        return (<DropdownLink caret={false} title={<StyledEventNode text={text} hoverText={hoverText} type={type}/>} anchorRight={anchor === 'right'}>
        {errors.slice(0, numEvents).map(function (error, i) {
                var target = generateSingleErrorTarget(error, organization, location, errorDest);
                return (<DropdownNodeItem key={error.event_id} event={error} onSelect={function () { return handleDropdownItem(target, nodeKey, organization, false); }} first={i === 0} organization={organization} subtext="error" subtextType="error" anchor={anchor}/>);
            })}
        {events.slice(0, numEvents).map(function (event, i) {
                var target = generateSingleTransactionTarget(event, organization, location, transactionDest);
                return (<DropdownNodeItem key={event.event_id} event={event} onSelect={function () { return handleDropdownItem(target, nodeKey, organization, false); }} first={i === 0 && errors.length === 0} organization={organization} subtext={getDuration(event['transaction.duration'] / 1000, event['transaction.duration'] < 1000 ? 0 : 2, true)} subtextType="default" anchor={anchor}/>);
            })}
        {events.length > numEvents && hoverText && extrasTarget && (<DropdownItem onSelect={function () { return handleDropdownItem(extrasTarget, nodeKey, organization, true); }}>
            {hoverText}
          </DropdownItem>)}
      </DropdownLink>);
    }
}
function DropdownNodeItem(_a) {
    var event = _a.event, onSelect = _a.onSelect, first = _a.first, organization = _a.organization, subtext = _a.subtext, subtextType = _a.subtextType, anchor = _a.anchor;
    return (<DropdownItem onSelect={onSelect} first={first}>
      <DropdownItemSubContainer>
        <Projects orgId={organization.slug} slugs={[event.project_slug]}>
          {function (_a) {
            var projects = _a.projects;
            var project = projects.find(function (p) { return p.slug === event.project_slug; });
            return (<ProjectBadge hideName project={project ? project : { slug: event.project_slug }} avatarSize={16}/>);
        }}
        </Projects>
        <StyledTruncate value={event.transaction} 
    // expand in the opposite direction of the anchor
    expandDirection={anchor === 'left' ? 'right' : 'left'} maxLength={35} leftTrim trimRegex={/\.|\//g}/>
      </DropdownItemSubContainer>
      <SectionSubtext type={subtextType}>{subtext}</SectionSubtext>
    </DropdownItem>);
}
function StyledEventNode(_a) {
    var text = _a.text, hoverText = _a.hoverText, to = _a.to, onClick = _a.onClick, _b = _a.type, type = _b === void 0 ? 'white' : _b;
    return (<Tooltip position="top" containerDisplayMode="inline-flex" title={hoverText}>
      <EventNode type={type} icon={null} to={to} onClick={onClick}>
        {text}
      </EventNode>
    </Tooltip>);
}
var HIDE_MISSING_SERVICE_KEY = 'quick-trace:hide-missing-services';
// 30 days
var HIDE_MISSING_EXPIRES = 1000 * 60 * 60 * 24 * 30;
function readHideMissingServiceState() {
    var value = localStorage.getItem(HIDE_MISSING_SERVICE_KEY);
    if (value === null) {
        return false;
    }
    var expires = parseInt(value, 10);
    var now = new Date().getTime();
    return expires > now;
}
var MissingServiceNode = /** @class */ (function (_super) {
    __extends(MissingServiceNode, _super);
    function MissingServiceNode() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.state = {
            hideMissing: readHideMissingServiceState(),
        };
        _this.dismissMissingService = function () {
            var _a = _this.props, organization = _a.organization, platform = _a.platform;
            var now = new Date().getTime();
            localStorage.setItem(HIDE_MISSING_SERVICE_KEY, (now + HIDE_MISSING_EXPIRES).toString());
            _this.setState({ hideMissing: true });
            trackAnalyticsEvent({
                eventKey: 'quick_trace.missing_service.dismiss',
                eventName: 'Quick Trace: Missing Service Dismissed',
                organization_id: parseInt(organization.id, 10),
                platform: platform,
            });
        };
        _this.trackExternalLink = function () {
            var _a = _this.props, organization = _a.organization, platform = _a.platform;
            trackAnalyticsEvent({
                eventKey: 'quick_trace.missing_service.docs',
                eventName: 'Quick Trace: Missing Service Clicked',
                organization_id: parseInt(organization.id, 10),
                platform: platform,
            });
        };
        return _this;
    }
    MissingServiceNode.prototype.render = function () {
        var hideMissing = this.state.hideMissing;
        var _a = this.props, anchor = _a.anchor, connectorSide = _a.connectorSide;
        if (hideMissing) {
            return null;
        }
        // TODO(wmak): Replace doc link with one that is either platform specific or platform agnostic
        return (<React.Fragment>
        {connectorSide === 'left' && <TraceConnector />}
        <DropdownLink caret={false} title={<EventNode type="white">???</EventNode>} anchorRight={anchor === 'right'}>
          <DropdownItem first width="small">
            <ExternalDropdownLink href="https://docs.sentry.io/platforms/javascript/performance/connect-services/" onClick={this.trackExternalLink}>
              {t('Connect to a service')}
            </ExternalDropdownLink>
          </DropdownItem>
          <DropdownItem onSelect={this.dismissMissingService} width="small">
            {t('Dismiss')}
          </DropdownItem>
        </DropdownLink>
        {connectorSide === 'right' && <TraceConnector />}
      </React.Fragment>);
    };
    return MissingServiceNode;
}(React.Component));
//# sourceMappingURL=index.jsx.map