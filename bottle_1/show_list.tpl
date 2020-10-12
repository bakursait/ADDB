<p>Todo List</p>
<table border="1">
%for row in rows:
    <tr>
    %for item in row[1:]:
        <td>{{item}}</td>
    %end
        <td>
            <a href="/delete_item/{{row[0]}}">Delete</>
        </td>
    %end
    </tr>
%end
</table>

<a href="/new_item">Add New Item..</>
