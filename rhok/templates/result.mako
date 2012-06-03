% if not items:
    <p>No disorders matched for your child.</p>
% else:
    <p>You child displays symptons of:</p>

    <ul>
    % for item in items:
        <li>${item}</li>
    % endfor
    </ul>
% endif
