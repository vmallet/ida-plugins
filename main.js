
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

/** Src filter. */
let src = [];
const src_checkboxes = [ "#src-cpp", "#src-py" ];

/** Category filter. */
let cats = [];
const cats_checkboxes = [
		"#cats-collab", "#cats-deobf", "#cats-decomp", "#cats-loader",
	    "#cats-debug", "#cats-proc", "#cats-trace", "#cats-ui" ];

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
