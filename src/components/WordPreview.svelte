<script lang='ts'>
    import * as d3 from 'd3';
    import cloud from 'd3-cloud';
    import { onMount, afterUpdate} from 'svelte';
    import { wordCloudDataModels } from '../store';

    const svg_width:number = 600;
    const svg_height:number = 350;

    const margin = {top: 0, right: 70, bottom: 40, left: 40};
    let width:number = svg_width - margin.left - margin.right;
    let height:number = svg_height - margin.top - margin.bottom;


    afterUpdate(async()=>{
        // set the dimensions and margins of the graph
        
		const cloudDiv = document.querySelector('#cloud');
		width = cloudDiv?.parentElement?.offsetWidth??width - margin.left - margin.right;
		height = cloudDiv?.parentElement?.offsetHeight??height - margin.top - margin.bottom;
		cloudDiv?.firstElementChild?.setAttribute("width", (width).toString());
		cloudDiv?.firstElementChild?.setAttribute("height", height.toString());
    });

    onMount(()=>{
        const myWords = JSON.parse(JSON.stringify($wordCloudDataModels)).map((obj: { rank: number; word: string; count: number; is_not_risk: boolean; }) => {
            return {
                "rank" : obj.rank,
                "word" : obj.word,
                "size" : obj.count,
                "is_not_risk" : obj.is_not_risk
            }
        });

        let wordSorted = myWords.sort((a, b) => b.size - a.size);
        wordSorted = wordSorted.slice(0, 5);
        // append the svg object to the body of the page
        var svg = d3.select("#cloud")
                    .append("div")
                        .classed("container", true)
                    .append("svg")
                        .attr("preserveAspectRatio", "xMinYMin meet")
                        .attr("width", width)
                        .attr("height", height)
                        .attr("viewBox", `50 0 200 300`)
                        .classed("chart", true)
                    .append("g")
                        .attr("transform",
                            "translate(" + margin.left + "," + margin.top + ")");


        const sizeScale = d3.scaleLinear()
                    .range([15, 55])
                    .domain([1, Math.max.apply(null, myWords.map(wordObj => wordObj.size))])

        // Constructs a new cloud layout instance. It run an algorithm to find the position of words that suits your requirements
        // Wordcloud features that are different from one word to the other must be here
        var layout = cloud()
                    .size([width, height])
                    .words(wordSorted.map(function(d) { return {text: d.word, size:d.size, is_not_risk:d.is_not_risk}; }))
                    .padding(10)        //space between words
                    .rotate(function() { return ~~(Math.random() * 2) * 90; })
                    .fontSize(function(d) { return sizeScale(d.size); })      // font size of words
                    .on("end", draw);
        layout.start();


        // This function takes the output of 'layout' above and draw the words
        // Wordcloud features that are THE SAME from one word to the other can be here
        function draw(words) {
            svg.append("g")
                .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
                .attr("id", "cloud_content")
                .selectAll("text")
                    .data(words)
                .enter().append("text")
                    .style("font-size", function(d) { return d.size; })
                    .style("fill", d => {
                        return d.is_not_risk ? "var(--positive-color)" : "var(--negative-color)"})
                    .attr("text-anchor", "middle")
                    .style("font-family", "Impact")
                    .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                    })
                    .text(function(d) { return d.text; });
            
            }
        
    });

</script>

<div id="cloud"></div>

<style>
    .container{
        display: inline-block;
        position: relative;
        width: 100%;
        padding-bottom: 100%; /* aspect ratio */
        vertical-align: top;
        overflow: hidden;
    }
    .chart {
        display: inline-block;
        position: absolute;
        top: 0;
        left: 0;
    }
</style>