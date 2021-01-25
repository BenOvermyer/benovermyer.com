const search = instantsearch({
    appId: "VSB6H6YI4R",
    apiKey: "0d1788fa3149085381f23b4573d3f42a",
    indexName: "main",
    routing: true,
});

// initialize SearchBox
search.addWidget(
    instantsearch.widgets.pagination({
        container: "#pagination-container",
        maxPages: 20,
        // default is to scroll to 'body', here we disable this behavior
        scrollTo: false,
        showFirstLast: false,
    })
);

search.addWidget(
    instantsearch.widgets.searchBox({
        container: "#search-box",
        placeholder: "Search my site",
    })
);

search.addWidget(
    instantsearch.widgets.hits({
        container: "#hits",
        templates: {
            item:
                '<div class="search-result"><p><a href="{{url}}">{{title}}</a></p> <p>{{description}}</p></div>',
        },
    })
);

search.start();
