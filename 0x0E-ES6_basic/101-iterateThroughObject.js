export default function iterateThroughObject(reportWithIterator) {
	const employees = [];
	for (const r of reportWithIterator) {
		employees.push(r);
	}

	return employees.join(' | ');
}
