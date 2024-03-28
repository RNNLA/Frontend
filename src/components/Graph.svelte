<script>
    import { onMount } from 'svelte';
  
    // 예시 데이터
    let data = [
      { date: '2024-03-20', positive: 40, negative: 60 },
      { date: '2024-03-21', positive: 30, negative: 70 },
      { date: '2024-03-22', positive: 50, negative: 50 },
      { date: '2024-03-23', positive: 20, negative: 80 },
      { date: '2024-03-24', positive: 60, negative: 40 },
      { date: '2024-03-25', positive: 70, negative: 30 },
      { date: '2024-03-26', positive: 80, negative: 20 },
    ];
  
    onMount(() => {
      // D3 차트 생성 함수
      const createChart = () => {
        const d3 = window.d3; // D3 참조
        const width = 400;
        const height = 300;
        const margin = { top: 20, right: 20, bottom: 100, left: 40 };
        const chartWidth = width - margin.left - margin.right;
        const chartHeight = height - margin.top - margin.bottom;
  
        // SVG 요소 생성
        const svg = d3.select('#chart')
          .append('svg')
          .attr('width', width)
          .attr('height', height)
          .append('g')
          .attr('transform', `translate(${margin.left},${margin.top})`);
  
        // 축 및 스케일 설정
        const x = d3.scaleBand()
          .range([0, chartWidth])
          .domain(data.map(d => d.date))
          .padding(0.1);
        
        const y = d3.scaleLinear()
          .range([chartHeight, 0])
          .domain([0, 100]);
  
        // 축 추가
        svg.append('g')
          .attr('transform', `translate(0,${chartHeight})`)
          .call(d3.axisBottom(x));
  
        svg.append('g')
          .call(d3.axisLeft(y));
  
        // 막대 추가
        svg.selectAll('.bar')
          .data(data)
          .enter().append('rect')
          .attr('class', 'bar')
          .attr('x', d => x(d.date))
          .attr('y', d => y(d.positive))
          .attr('width', x.bandwidth())
          .attr('height', d => chartHeight - y(d.positive))
          .attr('fill', 'steelblue');
      };
  
      createChart();
    });
  </script>
  
  <!-- 차트를 표시할 요소 -->
  <div id="chart"></div>