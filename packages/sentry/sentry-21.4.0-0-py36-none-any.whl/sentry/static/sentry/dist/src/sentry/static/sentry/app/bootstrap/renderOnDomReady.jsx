export function renderOnDomReady(renderFn) {
    if (document.readyState === 'complete') {
        renderFn();
    }
    else {
        document.addEventListener('DOMContentLoaded', renderFn);
    }
}
//# sourceMappingURL=renderOnDomReady.jsx.map