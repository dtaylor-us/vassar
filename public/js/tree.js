document.addEventListener("DOMContentLoaded", async () => {
    // Fetch the data from the backend
    const response = await fetch("/tree");
    const data = await response.json();

    const width = 1200;
    const height = 1000;
    const margin = {top: 20, right: 120, bottom: 20, left: 120};

    const svg = d3
        .select("#family-tree")
        .append("svg")
        .attr("width", width + margin.right + margin.left)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    const root = d3.hierarchy(data);

    const treeLayout = d3.tree().size([height, width]);

    treeLayout(root);

    // Links
    svg.selectAll("path")
        .data(root.links())
        .enter()
        .append("path")
        .attr("d", d3.linkHorizontal()
            .x(d => d.y)
            .y(d => d.x)
        )
        .attr("fill", "none")
        .attr("stroke", "#ccc");

    // Nodes
    const node = svg.selectAll("g.node")
        .data(root.descendants())
        .enter()
        .append("g")
        .attr("class", "node")
        .attr("transform", d => `translate(${d.y},${d.x})`);

    node.append("circle")
        .attr("r", 5)
        .attr("fill", "#ff5722");

    node.append("text")
        .attr("dy", ".35em")
        .attr("x", d => d.children ? -10 : 10)
        .style("text-anchor", d => d.children ? "end" : "start")
        .text(d => d.data.name);
});
