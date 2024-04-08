<script lang="ts">
    import {createEventDispatcher} from 'svelte'

    import ItemDirection from "./ItemDirection.svelte";
    import checkMark from "$lib/images/checkmark.svg";
    import Spacer from "./Spacer.svelte";
    export let isPositive : boolean = true;
    export let isChecked : boolean = false;
    export let isDisabled : boolean = false;
    export let title : string = '제목설정';
    export let buttonKey : string = '';
    const dispatch = createEventDispatcher();
    function handleClick() {
        dispatch('click', { 
            buttonKey : buttonKey,
            isChecked : isChecked 
        });
    }
</script>
    <button on:click={handleClick}>
        <ItemDirection direction="row" enableCenter={true}>
            <img src={checkMark} alt="check mark" class="{isChecked? isPositive? 'checked-positive' : 'checked-negative' : ''} {isDisabled? 'disabled':''}" >
            <Spacer width={.8}></Spacer>
            <div class="{isDisabled? 'disabled': ''}">
                {title}
            </div>
        </ItemDirection>
    </button>


<style>
    img {
        width: 2.5rem;
        height: 2.5rem;
        background-color: #D9D9D9;
        border-radius: 0.5rem;
    }
    img.disabled {
        background-color: rgba(217,217,217,.5);
    }
    .disabled {
        color: rgba(217,217,217,.5);
    }
    .checked-positive {
        background-color: #98C039;
    }
    .checked-negative {
        background-color: #D43C36;
    }
    button {
        font-size : 2rem;
        background-color: transparent;
        border: none;
        font-weight: 700;
    }
</style>