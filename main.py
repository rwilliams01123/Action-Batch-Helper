import batch_helper
import meraki


def merakiActionBatch(objlist, organization_id, dashboard):

    # create some action lists
    action_list_1 = list()
    action_list_2 = list()
    action_list_3 = list()
    all_actions = list()

    for i in objlist:
        action1 = dashboard.batch.#api_call
        action_list_1.append(action1)

        action2 = dashboard.batch.#api_call
        action_list_2.append(action2)

        action3 = dashboard.batch.#api_call
        action_list_3.append(action3)

    all_actions.extend(action_list_1)
    all_actions.extend(action_list_2)
    all_actions.extend(action_list_3)

    ### SECTION: Template using submodule 'batch_helper' to prepare and
    ###            execute the API call

    print('\nPreparing action batch call for '
          f'{len(all_actions)} total actions\n')

    test_helper = batch_helper.BatchHelper(
        dashboard,
        organization_id,
        all_actions,
        linear_new_batches=True,
        actions_per_new_batch=100)

    test_helper.prepare()
    test_helper.generate_preview()
    test_helper.execute()

    print(f'Helper status is {test_helper.status}')

    batches_report = dashboard.organizations.getOrganizationActionBatches(
        organization_id)
    new_batches_statuses = [
        {
            'id': batch['id'],
            'status': batch['status']
        } for batch in batches_report
        if batch['id'] in test_helper.submitted_new_batches_ids
    ]
    failed_batch_ids = [
        batch['id'] for batch in new_batches_statuses
        if batch['status']['failed']
    ]
    if failed_batch_ids:
        print(f'Failed batch IDs are as follows: {failed_batch_ids}')
    else:
        print('\n\n\n')
