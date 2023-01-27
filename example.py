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
    #
    batch_helper.ActionBatch(dashboard, org_id, all_actions)
