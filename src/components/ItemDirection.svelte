<script lang="ts">
    export let direction :string = "column";
    export let enableCenter:Boolean = false;
    export let enableExpand:Boolean = false;
    export let enableSpaceBetween:Boolean = false;
    export let enableMax:Boolean = false;
    export let style = {};
	
    let clazz : String = '';
    export { clazz as class}; 

    const formatToHTMLStyleFromObject = (styleObj : Object) => {
        return Object.entries(style).reduce((acc, [key, value]) => `${acc} ${key}: ${value};`, '');
    };

    $: styleHTML = formatToHTMLStyleFromObject(style);
</script>

<div class="{direction} {clazz} {enableCenter ? 'center':''} {enableExpand ? 'expand' : ''} {enableSpaceBetween ? 'space-between' : ''} {enableMax ? 'max' : ''}" style={styleHTML}>
    <slot></slot>
</div>

<style>
    .column {
        display: flex;
        flex-direction: column;
    }
    .max {
        height: 100vh;
        width: 100%;
    }
    .row {
        display: flex;
        flex-direction: row;
    }
    .center {
        justify-content: center;
        align-items: center;
    }
    .expand {
        flex-grow: 1;
    }
    .space-between {
        justify-content: space-between;
    }
</style>
