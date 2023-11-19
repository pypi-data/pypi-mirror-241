# NoteVault

Define a schema over markdown documents and store certain sections as columsn in sqlite database.

Every list item must have a `name` as unique key. For non-list items the key is the heading.

## Format
Sections are defined by headings.
key-value pairs are extracted into fields, e.g. `key: value`
Fields (extraction units) correspond to "Tags", e.g. `li, h2`
because it can contain other tags and newlines.
field values with commas must be quoted: `participants: '@user1, @user2'`

### Single Item:
- spec: `is_list: false`
- markdown lists as fields: `- key: value`

### Multiple Items:
- spec: `is_list: true`

#### sub-headings
- spec: `is_list: true` + `heading_field: name` (must specify the field which will hold the sub-heading in the schema)
- substructure: format: `## Title x`
can contain:
- markdown lists as fields: `- key: value`
- sub-headings as simple content fields

#### markdown lists
- substructure: format: `- key: value, key: value, key: "complex, value"`


# TODO
- define sections via headings
- parse every section into one model generically (look for props, try to avoid document hierarchy)
