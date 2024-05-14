<script lang='ts'>
    import * as d3 from 'd3';
    import cloud from 'd3-cloud';
    import { onMount, afterUpdate} from 'svelte';

    const svg_width:number = 600;
    const svg_height:number = 350;

    const margin = {top: 0, right: 70, bottom: 40, left: 40};
    let width:number = svg_width - margin.left - margin.right;
    let height:number = svg_height - margin.top - margin.bottom;


    const myWords = [
        { word: "Word0", size: 300, is_not_risk: true },
        { word: "Word1", size: 100, is_not_risk: true },
        { word: "Word2", size: 200, is_not_risk: false },
        { word: "Word3", size: 100, is_not_risk: true },
        { word: "Word4", size: 500, is_not_risk: true },
        { word: "Word5", size: 110, is_not_risk: false },
        { word: "Word6", size: 68, is_not_risk: true },
        { word: "Word7", size: 40, is_not_risk: true },
        { word: "Word8", size: 30, is_not_risk: false },
        { word: "Word9", size: 10, is_not_risk: true },
        { word: "Word10", size: 1, is_not_risk: false },
        { word: "Word11", size: 2, is_not_risk: true },
        { word: "Word12", size: 3, is_not_risk: true },
        { word: "Word13", size: 4, is_not_risk: true },
        { word: "Word14", size: 5, is_not_risk: false },
        { word: "Word15", size: 6, is_not_risk: true },
        { word: "Word16", size: 7, is_not_risk: true },
    ];

    let wordSorted = myWords.sort((a, b) => b.size - a.size);
    wordSorted = wordSorted.slice(0, 5);

    afterUpdate(async()=>{
        // set the dimensions and margins of the graph
        
		const cloudDiv = document.querySelector('#cloud');
		width = cloudDiv?.parentElement?.offsetWidth??width - margin.left - margin.right;
		height = cloudDiv?.parentElement?.offsetHeight??height - margin.top - margin.bottom;
		cloudDiv?.firstElementChild?.setAttribute("width", (width).toString());
		cloudDiv?.firstElementChild?.setAttribute("height", height.toString());
    });

    onMount(()=>{
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