<script lang='ts'>
    import {data_format} from '../store';
    let todayName = data_format('WordCloud','.png');
    let dataPath = '/data/' + todayName;

</script>

<div id="cloud"><img src={dataPath} alt="WordCloud"/></div>

<style>

</style>