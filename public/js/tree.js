document.addEventListener("DOMContentLoaded", async () => {
    // Fetch the data from the backend
    const response = await fetch("/tree");
    const data = await response.json();

    const width = 1200;
    const height = 1200;
    const margin = {top: 40, right: 120, bottom: 20, left: 120};
    const cardWidth = 150;
    const cardHeight = 50;
    // Define the background color here
    const backgroundColor = "#1c1c1c";  // Use the color from the uploaded image

    const svg = d3
        .select("#family-tree")
        .append("svg")
        .attr("width", width + margin.right + margin.left)
        .attr("height", height + margin.top + margin.bottom)
        .style("background-color", backgroundColor)  // Set the background color
        .call(d3.zoom().on("zoom", function(event) {
            svg.attr("transform", event.transform);
        }))
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    const root = d3.hierarchy(data);
    root.x0 = height / 2;
    root.y0 = 0;

    // Tree layout with increased separation between columns
    const treeLayout = d3.tree()
        .size([height, width - margin.left - margin.right])
        .separation((a, b) => (a.parent === b.parent ? 2 : 3)); // Increase separation between sibling nodes

    const update = (source) => {
        // Assign the new positions for the nodes
        treeLayout(root);

        const nodes = root.descendants();
        const links = root.descendants().slice(1);

        // Adjust y position to increase space between columns
        nodes.forEach(d => {
            d.y = d.depth * 250;  // Increase horizontal spacing by adjusting depth multiplier
            d.x *= 1.5;  // Increase vertical spacing by scaling the x position
        });

        // Update the nodes
        const node = svg.selectAll("g.node")
            .data(nodes, d => d.id || (d.id = ++i));

        const nodeEnter = node.enter().append("g")
            .attr("class", "node")
            .attr("transform", d => `translate(${source.y0},${source.x0})`)
            .on("click", click);

        nodeEnter.append("rect")
            .attr("width", cardWidth)
            .attr("height", cardHeight)
            .attr("x", -cardWidth / 2)
            .attr("y", -cardHeight / 2)
            .attr("fill", d => d._children ? "#ff5722" : "#ffccbc")
            .attr("stroke", "steelblue")
            .attr("stroke-width", "2px")
            .attr("rx", 10)
            .attr("ry", 10);

        nodeEnter.append("text")
            .attr("dy", ".35em")
            .attr("x", 0)
            .attr("text-anchor", "middle")
            .attr("fill", "#000")
            .text(d => d.data.name);

        const nodeUpdate = nodeEnter.merge(node);

        nodeUpdate.transition()
            .duration(750)
            .attr("transform", d => `translate(${d.y},${d.x})`);

        nodeUpdate.select("rect")
            .attr("fill", d => d._children ? "#ff5722" : "#ffccbc");

        nodeUpdate.select("text")
            .style("fill-opacity", 1);

        const nodeExit = node.exit().transition()
            .duration(750)
            .attr("transform", d => `translate(${source.y},${source.x})`)
            .remove();

        nodeExit.select("rect")
            .attr("width", 1e-6)
            .attr("height", 1e-6);

        nodeExit.select("text")
            .style("fill-opacity", 1e-6);

        // Update the links
        const link = svg.selectAll("path.link")
            .data(links, d => d.id);

        const linkEnter = link.enter().insert("path", "g")
            .attr("class", "link")
            .attr("d", d => {
                const o = {x: source.x0, y: source.y0};
                return diagonal({source: o, target: o});
            })
            .attr("fill", "none")
            .attr("stroke", "#ccc")
            .attr("stroke-width", "2px");

        const linkUpdate = linkEnter.merge(link);

        linkUpdate.transition()
            .duration(750)
            .attr("d", d => diagonal({source: d.parent, target: d}));

        const linkExit = link.exit().transition()
            .duration(750)
            .attr("d", d => {
                const o = {x: source.x, y: source.y};
                return diagonal({source: o, target: o});
            })
            .remove();

        nodes.forEach(d => {
            d.x0 = d.x;
            d.y0 = d.y;
        });
    };

    const click = (event, d) => {
        if (d.children) {
            d._children = d.children;
            d.children = null;
        } else {
            d.children = d._children;
            d._children = null;
        }
        update(d);
    };

    const collapse = (d) => {
        if (d.children) {
            d._children = d.children;
            d._children.forEach(collapse);
            d.children = null;
        }
    };

    const expandAll = () => {
        root.each(d => {
            if (d._children) {
                d.children = d._children;
                d._children = null;
            }
        });
        update(root);
    };

    d3.select("#expand-all").on("click", expandAll);

    const diagonal = d3.linkHorizontal()
        .x(d => d.y)
        .y(d => d.x);

    let i = 0;
    root.children.forEach(collapse); // Start with all nodes collapsed
    update(root);
});
