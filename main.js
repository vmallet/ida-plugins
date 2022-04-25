
let table = new Tabulator("#plugin-table", {
	data:tabledata, //load initial data into table
	layout:"fitColumns", //fit columns to width of table (optional)
	columns:[ //Define Table Columns
		{title:"Name", field: "name", sorter: "string", formatter:"link", hozAlign:"left",
			formatterParams: {urlField: "url", labelField: "name", target: "_blank"}, width: 150},
		{title:"Desc", field:"desc", sorter:"string", formatter: "textarea", hozAlign:"left"},
		{title:"Cat", field:"cats", sorter:"string", formatter: "textarea", hozAlign:"left", width: 100},
		{title:"Src", field:"src", sorter:"string", formatter: "plaintext", hozAlign:"left", width: 50},
		{title:"Updated", field:"last", sorter:"string", formatter:function(cell, params, onRendered){
				if (!cell.getValue()) {
					return "";
				}
		        return moment(cell.getValue(), "YYYYMMDD").fromNow();
		    },
			hozAlign:"left", width: 120}
	],
});
table.on("dataFiltered", function(filters, rows){
	updateStats(rows)
});

/** Src filter. */
let src = [];
const src_checkboxes = [ "#src-cpp", "#src-py" ];

/** Category filter. */
let cats = [];
const cats_checkboxes = [
		"#cats-collab", "#cats-debug", "#cats-decomp", "#cats-deobf", "#cats-dev",
		"#cats-int", "#cats-loader", "#cats-proc", "#cats-trace",
		"#cats-ui" ];

/**
 * Filter a table row.
 */
function customFilter(data) {
	if (src.length && !src.includes(data.src)) {
		return false;
	}
	// Note: this one only works because it is the last one in the chain.
	if (cats.length) {
		if (!data.cats) {
			return false;
		}
		for (const cat of cats) {
			if (data.cats.includes(cat)) {
				return true;
			}
		}
		return false;
	}
	return true;
}

/**
 * Super simple dictionary w/ default value. Not ideal but will get us by.
 */
class DefaultDict {
    constructor(defaultVal) {
        return new Proxy(
            {},
            {
                get: (target, name) => {
                    if (name === '__dict__') {
                        return target;
                    }
					if (name in target) {
                        return target[name];
                    }
					target[name] = defaultVal;
					return defaultVal;
                },
            }
        );
    }
}

/**
 * Return a custom string for the given key/value pair.
 */
function _kvToStr([k, v]) {
	if (k === "undefined") {
		return "(none):" + v;
	}
	return k + ":" + v;
}

/**
 * Compare two [name, count] pairs, putting any name starting with '(' last.
 *
 * (Not robust.)
 */
function _sortParenLast([a, c1], [b, c2]) {
	let res = 0;
	if (a < b) {
		res = -1;
	} else if (a > b) {
		res = 1;
	}

	if (a.startsWith('(') || b.startsWith('(')) {
		res = -res;
	}
	return res;
}

/**
 * Rename 'undefined' to (none).
 */
function map_undefined([name, count]) {
	return [ name === "undefined" ? "(none)" : name, count];
}

/**
 * Construct the stats text displayed above the table. Ultra crude.
 *
 * TODO: make this presentable, decide what to keep and what not to.
 * */
function buildStats(rows) {
	const count = rows.length
	const zsrcs = new DefaultDict(0);
	const zcats = new DefaultDict(0);

	// Count languages, categories
	for (const row of rows) {
		let data = row.getData();
		// Count source language, straightforward
		zsrcs[data.src]++;
		// Count categories
		if (!data.cats) {
			zcats["undefined"]++;
		} else {
			let split = data.cats.split(",");
			for (const cat of split) {
				zcats[cat.trim()]++;
			}
		}
	}

	src_stats = Object.entries(zsrcs).map(map_undefined).sort(_sortParenLast)
	cat_stats = Object.entries(zcats).map(map_undefined).sort(_sortParenLast)

	return { count, src_stats, cat_stats }
}

/**
 * Build and attach stat elements for the given counts to the parent element
 * with id 'parentId'.
 */
function populateStatElements(parentId, counts) {
	let $stats = $(parentId);
	$stats.empty()
	for (const [name, count] of counts) {
		$span = $("<span>", { "class": "stat-elem"})
	    $span.text(name + " ")
		$val = $("<span>", { "class": "stat-val"})
		$val.text(count)
		$span.append($val)
		$stats.append($span)
	}
}

/**
 * Update the "showing" stats when the table is changed.
 */
function updateStats(rows) {
	let { count, src_stats, cat_stats } = buildStats(rows)
	$("#plugin-count").text(count)
	populateStatElements("#stats-languages", src_stats)
	populateStatElements("#stats-categories", cat_stats)
	$("#loading").css("visibility", "hidden");
	$("#stats").css("visibility", "visible");
}

/**
 * Return the values associated with the checked checkboxes from the set
 * of checkboxes identified by ids.
 *
 * @param ids ids of checkboxes
 * @returns {[]} a list of values, possibly empty
 */
function getCheckedValues(ids) {
	vals = [];
	for (const id of ids) {
		let cb = $(id);
		if (cb.is(':checked')) {
			vals.push(cb.val());
		}
	}
	return vals;
}

/**
 * React to a filter-setup change and update the active filter accordingly.
 */
function updateFilter() {
	src = getCheckedValues(src_checkboxes);
	cats = getCheckedValues(cats_checkboxes);

	if (src.length || cats.length) {
		table.setFilter(customFilter);
	} else {
		table.clearFilter();
	}
	// A bit of a mystery why the table needs to be redrawn. Chalk it to my
	// lack of knowledge here...
	table.redraw();
}

/**
 * Make sure the elements corresponding to the given ids update the
 * filter on change.
 */
function registerUpdate(ids) {
	for (const id of ids) {
		$(id).change(updateFilter);
	}
}

registerUpdate(src_checkboxes);
registerUpdate(cats_checkboxes);
