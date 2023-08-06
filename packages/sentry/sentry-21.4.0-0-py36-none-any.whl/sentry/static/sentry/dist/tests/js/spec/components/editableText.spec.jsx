import React from 'react';
import { act } from 'react-dom/test-utils';
import { mountWithTheme } from 'sentry-test/enzyme';
import EditableText from 'app/components/editableText';
var createListenersMock = function (type) {
    var eventTarget = type === 'window' ? window : document;
    var listeners = [];
    var handler = function (eventData, event) {
        var _a, _b, _c, _d;
        var filteredListeners = listeners.filter(function (listener) {
            return listener.hasOwnProperty(event);
        });
        if ((eventData === null || eventData === void 0 ? void 0 : eventData.key) === 'Escape') {
            return (_b = (_a = filteredListeners[1]) === null || _a === void 0 ? void 0 : _a[event]) === null || _b === void 0 ? void 0 : _b.call(_a, eventData);
        }
        return (_d = (_c = filteredListeners[0]) === null || _c === void 0 ? void 0 : _c[event]) === null || _d === void 0 ? void 0 : _d.call(_c, eventData);
    };
    eventTarget.addEventListener = jest.fn(function (event, cb) {
        var _a;
        listeners.push((_a = {},
            _a[event] = cb,
            _a));
    });
    eventTarget.removeEventListener = jest.fn(function (event) {
        listeners = listeners.filter(function (listener) { return !listener.hasOwnProperty(event); });
    });
    return {
        mouseDown: function (domEl) { return handler({ target: domEl }, 'mousedown'); },
        keyDown: function (key) { return handler({ key: key }, 'keydown'); },
    };
};
function renderedComponent(onChange, newValue) {
    if (newValue === void 0) { newValue = 'bar'; }
    var currentValue = 'foo';
    var wrapper = mountWithTheme(<EditableText value={currentValue} onChange={onChange}/>);
    var content = wrapper.find('Content');
    expect(content.text()).toEqual(currentValue);
    var inputWrapper = wrapper.find('InputWrapper');
    expect(inputWrapper.length).toEqual(0);
    var styledIconEdit = wrapper.find('StyledIconEdit');
    expect(styledIconEdit).toBeTruthy();
    content.simulate('click');
    content = wrapper.find('Content');
    expect(inputWrapper.length).toEqual(0);
    inputWrapper = wrapper.find('InputWrapper');
    expect(inputWrapper).toBeTruthy();
    var styledInput = wrapper.find('StyledInput');
    expect(styledInput).toBeTruthy();
    styledInput.simulate('change', { target: { value: newValue } });
    var inputLabel = wrapper.find('InputLabel');
    expect(inputLabel.text()).toEqual(newValue);
    return wrapper;
}
describe('EditableText', function () {
    var currentValue = 'foo';
    var newValue = 'bar';
    it('edit value and click outside of the component', function () {
        var fireEvent = createListenersMock('document');
        var handleChange = jest.fn();
        var wrapper = renderedComponent(handleChange);
        act(function () {
            // Click outside of the component
            fireEvent.mouseDown(document.body);
        });
        expect(handleChange).toHaveBeenCalled();
        wrapper.update();
        var updatedContent = wrapper.find('Content');
        expect(updatedContent).toBeTruthy();
        expect(updatedContent.text()).toEqual(newValue);
    });
    it('edit value and press enter', function () {
        var fireEvent = createListenersMock('window');
        var handleChange = jest.fn();
        var wrapper = renderedComponent(handleChange);
        act(function () {
            // Press enter
            fireEvent.keyDown('Enter');
        });
        expect(handleChange).toHaveBeenCalled();
        wrapper.update();
        var updatedContent = wrapper.find('Content');
        expect(updatedContent).toBeTruthy();
        expect(updatedContent.text()).toEqual(newValue);
    });
    it('edit value and press escape', function () {
        var fireEvent = createListenersMock('window');
        var handleChange = jest.fn();
        var wrapper = renderedComponent(handleChange);
        act(function () {
            // Press escape
            fireEvent.keyDown('Escape');
        });
        expect(handleChange).toHaveBeenCalledTimes(0);
        wrapper.update();
        var updatedContent = wrapper.find('Content');
        expect(updatedContent).toBeTruthy();
        expect(updatedContent.text()).toEqual(currentValue);
    });
    it('clear value and show error message', function () {
        var fireEvent = createListenersMock('window');
        var handleChange = jest.fn();
        var wrapper = renderedComponent(handleChange, '');
        act(function () {
            // Press enter
            fireEvent.keyDown('Enter');
        });
        expect(handleChange).toHaveBeenCalledTimes(0);
        wrapper.update();
        var fieldControlErrorWrapper = wrapper.find('FieldControlErrorWrapper');
        expect(fieldControlErrorWrapper).toBeTruthy();
        expect(fieldControlErrorWrapper.text()).toEqual('Text required');
    });
});
//# sourceMappingURL=editableText.spec.jsx.map