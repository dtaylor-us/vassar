document.addEventListener("DOMContentLoaded", async () => {
  // Fetch the data from the backend
  const response = await fetch("/graph-data");
  const data = await response.json();

  // Utility function to truncate text
  function truncateText(text, maxLength) {
    return text.length > maxLength ? text.slice(0, maxLength) + '...' : text;
  }

  // Set the dimensions and radius of the sunburst
  const width = 928;
  const height = 928;
  const radius = Math.min(width, height) / 2;

  // Create the partition layout
  const partition = d3.partition()
    .size([2 * Math.PI, radius]);

  // Convert the data into a hierarchy and apply partition layout
  const root = partition(d3.hierarchy(data)
    .sum(d => d.value || 1) // Use value if present, otherwise 1 for equal sizing
    .sort((a, b) => b.value - a.value)
  );

  // Create a color scale based on the root author's children length
  const color = d3.scaleOrdinal(d3.quantize(d3.interpolateRainbow, data.children.length + 1));

  // Create the SVG container centered on the screen
  const svg = d3.select("#graph")
      .append("svg")
      .attr("width", width)
      .attr("height", height)
      .style("display", "block")
      .style("margin", "0 auto")
      .append("g")
      .attr("transform", `translate(${width / 2},${height / 2})`);

  // Define the arc generator with padding for visual separation
  const arc = d3.arc()
    .startAngle(d => d.x0)
    .endAngle(d => d.x1)
    .padAngle(d => Math.min((d.x1 - d.x0) / 2, 0.005))
    .padRadius(radius / 2)
    .innerRadius(d => d.y0)
    .outerRadius(d => d.y1 - 1);

  // Create a tooltip div that is hidden by default
  const tooltip = d3.select("body").append("div")
    .style("position", "absolute")
    .style("visibility", "hidden")
    .style("background", "#fff")
    .style("border", "1px solid #ccc")
    .style("padding", "8px")
    .style("border-radius", "4px")
    .style("box-shadow", "0px 0px 10px rgba(0, 0, 0, 0.1)")
    .style("font-family", "sans-serif")
    .style("font-size", "12px");

  // Draw the arcs (sunburst segments)
  svg.append("g")
    .attr("fill-opacity", 0.6)
    .selectAll("path")
    .data(root.descendants().filter(d => d.depth))
    .join("path")
    .attr("fill", d => { while (d.depth > 1) d = d.parent; return color(d.data.name); })
    .attr("d", arc)
    .on("mouseover", function(event, d) {
      tooltip.style("visibility", "visible")
        .text(d.data.name); // Display the full text in the tooltip
      d3.select(this).attr("fill", d3.rgb(color(d.data.name)).darker(0.5));
    })
    .on("mousemove", function(event) {
      tooltip.style("top", (event.pageY - 10) + "px")
        .style("left", (event.pageX + 10) + "px");
    })
    .on("mouseout", function(event, d) {
      tooltip.style("visibility", "hidden");
      d3.select(this).attr("fill", color(d.data.name));
    });

  // Add text labels with truncation and proper rotation and alignment
  svg.append("g")
    .attr("pointer-events", "none")
    .attr("text-anchor", "middle")
    .attr("font-size", 10)
    .attr("font-family", "sans-serif")
    .selectAll("text")
    .data(root.descendants().filter(d => d.depth && (d.y0 + d.y1) / 2 * (d.x1 - d.x0) > 10))
    .join("text")
    .attr("transform", function(d) {
      const x = (d.x0 + d.x1) / 2 * 180 / Math.PI;
      const y = (d.y0 + d.y1) / 2;
      return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`;
    })
    .attr("dy", "0.35em")
    .text(d => truncateText(d.data.name, 15)) // Truncate the text if necessary
    .append("title")
    .text(d => d.data.name); // Ensure full text appears on hover
});

