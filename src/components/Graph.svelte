
<script lang="ts">
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
  
    // 예시 데이터
    let data = [
      {date: '24-03-20',positive: 40, negative: 60, positive_data: 100, negative_data: 200},
      {date: '24-03-21',positive: 30, negative: 70, positive_data: 100, negative_data: 200},
      {date: '24-03-22',positive: 50, negative: 50, positive_data: 100, negative_data: 200},
      {date: '24-03-23',positive: 20, negative: 80, positive_data: 100, negative_data: 200},
      {date: '24-03-24',positive: 60, negative: 40, positive_data: 100, negative_data: 200},
      {date: '24-03-25',positive: 70, negative: 30, positive_data: 100, negative_data: 200},
      {date: '24-03-26',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-03-27',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-03-28',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-03-29',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-03-30',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-03-31',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-01',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-02',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-03',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-04',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-05',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-06',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-07',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      // {date: '24-03-26',positive: 80, negative: 20},
      // {date: '24-03-26',positive: 80, negative: 20},
      // {date: '24-03-26',positive: 80, negative: 20},
      // {date: '24-03-26',positive: 80, negative: 20},
      // {date: '24-03-26',positive: 80, negative: 20},
      // {date: '24-03-26',positive: 80, negative: 20},
    ];

    export let svg_width:Number = 400;
    export let svg_height:Number = 300;

    


    onMount(() => {
      const colors = ["#98C039", "#D43C36"];
      const highlight_colors = ["", ""]
      const margin = { top: 20, right: 20, bottom: 100, left: 40 };
      const width:Number = svg_width - margin.left - margin.right;
      const height:Number = svg_height - margin.top - margin.bottom;

      const svg = d3.select('#chart')
                  .append('svg')
                  .attr('width', svg_width)
                  .attr('hieght', svg_height)
                  .attr('viewBox', `0 0 ${svg_width} ${svg_height}`)

      const chart = svg.append('g')
                  .attr('transform', `translate(${margin.left},${margin.top})`)
                  .classed("chart_content", true);

      const x = d3.scaleBand().range([0, width]).domain(data.map(d => d.date)).padding(0.2);
      const y = d3.scaleLinear().range([height, 0]).domain([0, 100]);

      const keys = ['positive', 'negative'];
      const stacked_data = d3.stack().keys(keys)(data);

      // x axis
      chart.append('g')
          .attr('transform', `translate(0,${height})`)
          .call(d3.axisBottom(x))
          .classed('x_axis', true);

      chart.select('.x_axis')
          .attr("text-anchor", "end")
          .selectAll("text")
          .attr("transform", "rotate(-90)")
          .attr("dy", "-0.5em")
          .attr("dx", "-1em")
      
      // y axis
      chart.append('g')
          .call(d3.axisLeft(y))
          .classed('y_axis', true);


      
      
      // Drawing Chart
      const layers = chart.selectAll('.layer')
                      .data(stacked_data)
                      .enter()
                      .append('g')
                      .classed('layer', true)
                      .style('fill', (d,i) => colors[i])
                        .selectAll('rect')
                        .data(d => d)
                        .enter()
                        .append('rect')
                        .attr('y', d => y(d[1]))
                        .attr('x', d => x(d.data.date))
                        .attr('width', x.bandwidth())
                        .attr('height', d => y(d[0]) - y(d[1]))
                        .classed("bar", true)
                        .on("mouseover", onMouseOver)
                        .on("mouseout", onMouseOut);

      function onMouseOver(event, d){
        const self = event.target;
        let color = "";
        d3.select(self)
          .style("fill", ()=>{
            color = (d[0] == 0 ? "#4F641A" : "#691A16");
            return color;
          })

        const text = chart.append('g')
        
        
        text.append("rect")
            .attr("x",() => x(d3.select(self).datum().data.date) - x.bandwidth()/2)
            .attr("y",() => y(d3.select(self).datum()[1]) + (y(d3.select(self).datum()[0]) - y(d3.select(self).datum()[1]))/3)
            .attr("rx", 20)
            .attr("ry", 20)
            .attr("id", "popup_box")
            .attr("width", x.bandwidth()+40)
            .attr("height", "4em")
            .style("stroke-width", "3px")
            .style("stroke",color)
            .style('fill', "white")
          
          text.append("text")
              .text(`긍정 기사 : ${d3.select(self).datum().data.positive_data}건`)
              .attr("x",() => x(d3.select(self).datum().data.date) - x.bandwidth()/2+5)
              .attr("y",() => y(d3.select(self).datum()[1]) + (y(d3.select(self).datum()[0]) - y(d3.select(self).datum()[1]))/3+25)
              .attr("id", "popup_box");
          
          text.append("text")
              .text(`부정 기사 : ${d3.select(self).datum().data.negative_data}건`)
              .attr("x",() => x(d3.select(self).datum().data.date) - x.bandwidth()/2+5)
              .attr("y",() => y(d3.select(self).datum()[1]) + (y(d3.select(self).datum()[0]) - y(d3.select(self).datum()[1]))/3+50)
              .attr("id", "popup_box");
            
        // chart.append("text")
        //     .attr("x",() => x(d3.select(self).datum().data.date)-10)
        //     .attr("y",() => y(d3.select(self).datum()[1])+20) 
        //     .text(`부정 기사 : ${d3.select(self).datum().data.negative_data}건`);

        //     .attr("stroke","red")
        //     .attr("stroke-width",2)
        //     .text(d.x+","+d.y+","+d.r);
      }

      function onMouseOut(event, d){
        const self = event.target;
        d3.select(self)
          .style("fill", ()=>{
            return d[1] != 100 ? "#98C039" : "#D43C36";
            
          });
        
          d3.selectAll('#popup_box')
            .remove();
      }
    });
</script>
  
  <!-- 차트를 표시할 요소 -->
  <div id="chart">
  </div>

  <style>
    #popup_box{
    }

    .popup_text{

    }

  </style>


