document.addEventListener("DOMContentLoaded", async () => {
    // Fetch the data from the backend
    const response = await fetch("/tree");
    const data = await response.json();

    // Set up dimensions for the SVG
    const width = 1000;
    const height = 800;
    const margin = { top: 20, right: 120, bottom: 20, left: 120 };

    // Create the SVG element
    const svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    // Set up the tree layout
    const treeLayout = d3.tree().size([height - margin.top - margin.bottom, width - margin.left - margin.right]);

    // Convert the data into a hierarchy
    const root = d3.hierarchy(data);

    // Generate the tree structure
    const treeData = treeLayout(root);

    // Create links (lines connecting the nodes)
    const link = svg.selectAll(".link")
        .data(treeData.links())
        .enter().append("path")
        .attr("class", "link")
        .attr("d", d3.linkHorizontal()
            .x(d => d.y)
            .y(d => d.x))
        .style("fill", "none")
        .style("stroke", "#ccc")
        .style("stroke-width", "2px");

    // Create nodes
    const node = svg.selectAll(".node")
        .data(treeData.descendants())
        .enter().append("g")
        .attr("class", d => "node" + (d.children ? " node--internal" : " node--leaf"))
        .attr("transform", d => `translate(${d.y},${d.x})`);

    // Add circles for union nodes
    node.filter(d => d.data.type === "union")
        .append("circle")
        .attr("r", 10)
        .style("fill", "#6baed6")
        .style("stroke", "#3182bd")
        .style("stroke-width", "2px");

    // Add rectangles for individual nodes
    node.filter(d => d.data.type !== "union")
        .append("rect")
        .attr("width", 100)
        .attr("height", 20)
        .attr("y", -10)
        .attr("x", -50)
        .style("fill", d => d.data.gender === "Male" ? "#a1d99b" : "#fdae6b")
        .style("stroke", "#636363")
        .style("stroke-width", "1px");

    // Add labels to the nodes
    node.append("text")
        .attr("dy", ".35em")
        .attr("x", d => d.children ? -13 : 13)
        .style("text-anchor", d => d.children ? "end" : "start")
        .text(d => d.data.name)
        .style("font-size", "12px");

    // Add interactivity: zooming and panning
    const zoom = d3.zoom()
        .scaleExtent([0.5, 2])
        .on("zoom", (event) => {
            svg.attr("transform", event.transform);
        });

    d3.select("svg").call(zoom);
});
